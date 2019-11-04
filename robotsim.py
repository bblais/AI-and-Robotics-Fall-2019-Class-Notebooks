def Wait(seconds):
    import time     # import the time library for the sleep function
    time.sleep(seconds)

def closest_color_as_number(r,g,b,*args):

    min_distance_sq=0
    min_color=None
    for c,color in enumerate(args):
        r2,g2,b2=color
        distance_sq=(r-r2)**2+(g-g2)**2+(b-b2)**2

        if min_color is None:  # first color
            min_color=c
            min_distance_sq=distance_sq
        elif distance_sq<min_distance_sq:
            min_color=c
            min_distance_sq=distance_sq
        else:
            pass

    return min_color


def closest_color(r,g,b,**kwargs):
    """
    C=closest_color(100,0,0,
            red=[100,0,0],
            glreen=[0,100,0],
            black=[100,100,100],
            )
    """
    min_distance_sq=0
    min_color=None

    for color in kwargs:

        r2,g2,b2=kwargs[color]

        distance_sq=(r-r2)**2+(g-g2)**2+(b-b2)**2

        if min_color is None:  # first color
            min_color=color
            min_distance_sq=distance_sq
        elif distance_sq<min_distance_sq:
            min_color=color
            min_distance_sq=distance_sq
        else:
            pass

    return min_color

class Timer(object):
    def __init__(self,environment):
        self._reset()
        self.env=environment

    def _reset(self):
        self.t0=time.time()

    @property
    def time(self):
        self.env.update()
        return time.time()-self.t0

    @property
    def value(self):
        self.env.update()
        return time.time()-self.t0

    def seconds(self):
        self.env.update()
        return time.time()-self.t0    


class Sensor(object):

    def __init__(self,port,sensor_type):
        self.port=port
        self.name='S%c %s' % (port,sensor_type)
        self.type=sensor_type
        self._value=None
        self.env=None

    @property
    def value(self):
        self.env.update()
        return self._value
    
    @value.setter
    def value(self,v):
        self._value=v
        
        
    def __repr__(self):
        return self.name

class Motor(object):

    def __init__(self,port):
        self.port=port
        self.name='M%c' % (port)
        self.value=None
        self.env=None

        self._power=0
        self._position=0
        self.reset_position()

    def __repr__(self):
        return self.name
        
        
    def reset_position(self):
        self.position=0
        
    @property
    def position(self):
        self.env.update()
        return self._position
    
    @position.setter
    def position(self,pos):
        self._position=pos
    
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self,power):
        #print("before",power,self.power)
        self.env.update()
        #print("after",power,self.power)
        self._power=power
        if self._power>100:
            self._power=100
        if self._power<-100:
            self._power=-100


def Motors(port_letters,environment):
    m=[]
    unused=''
    ports=['A','B','C','D']
    for letter in port_letters:
        i=ord(letter.upper())-65
        m.append(Motor(ports[i]))
        
    for S in m:
        portnum=ord(S.port)-65+1
        environment.motors[portnum-1]=S
        S.env=environment
        
    if len(m)==0:
        return None
    elif len(m)==1:
        return m[0]
    else:
        return m

def Sensors(one=None,two=None,three=None,four=None,environment=None):

    sensors=[]
    for i,v in enumerate([one,two,three,four]):
        if not v:
            continue

        v=v.lower()

        ports=['1','2','3','4']

        if v=='us' or v.startswith('ultra'):
            sensors.append(Sensor(ports[i],'us'))
        elif v=='color':
            sensors.append(Sensor(ports[i],'color'))
        else:
            raise ValueError('Not implemented:' % v)

    for S in sensors:
        portnum=int(S.port)
        environment.sensors[portnum-1]=S
        S.env=environment
        
    if len(sensors)==0:
        return None
    elif len(sensors)==1:
        return sensors[0]
    else:
        
        return sensors
      
    
def flatten_alpha(im):
    from numpy import where,newaxis
    im=im[:,:,:3]+where(im[:,:,3]==1.0,0,1)[:, :, newaxis]
    return im


from pylab import imread,imshow,clf,plot,rand
import time

def randbetween(low,high):
    from pylab import rand
    return rand()*(high-low)+low

class Env(object):
    
    def __init__(self,imfname):
        
        self.image=imread(imfname)
        
        self.image=flatten_alpha(self.image)
        
        self.max_bot_speed=900/10.0 # pixels per second
        self.max_bot_speed=randbetween(70,120) # pixels per second
        
        self.motors=[None,None,None,None]
        self.sensors=[None,None,None,None]
        
        
        
        self.reset()
                
    def draw(self):
        self.update()
        
        clf()
        imshow(self.image)            
        x,y=[_[0] for _ in self.record],[_[1] for _ in self.record]
        
        plot([x],[y],'ro')
        
        
    def update_record(self):
        current_time=time.time()
        if current_time-self.last_record_time>0.1:
            self.last_record_time=current_time
            self.record.append(self.botpos[:])
        
    def update(self):
        current_time=time.time()
        try:
            dt=(current_time-self.last_time)
            dx=self.max_bot_speed*self.motors[0].power/100.0*dt
            
            self.botpos[0]+=dx
            self.botpos[1]+=self.drift
            #print("dx=",dx,"dt",dt,"power",self.motors[0].power)
            if self.botpos[0]<0:
                self.botpos[0]=0
            if self.botpos[0]>self.image.shape[1]:
                self.botpos[0]=self.image.shape[1]
            
        except AttributeError:
            pass
        
        
        if self.sensors[0] and self.sensors[0].type=='us':
            self.sensors[0].value=int(self.image.shape[1]-self.botpos[0])
        if self.sensors[1] and self.sensors[1].type=='color':
            try:
                self.sensors[1].value=list(self.image[int(self.image.shape[0]-self.botpos[1]),int(self.botpos[0]),:])
            except IndexError:
                self.sensors[1].value=None
                
        
        
        self.last_time=time.time()
        self.update_record()
        
    def reset(self):
        self.botpos=[50.0,self.image.shape[0]/3.0]
        self.botspeed=0
        self.drift=0.15
        self.start_time=time.time()
        self.last_time=time.time()
        self.last_record_time=time.time()
        self.record=[]

        self.update_record()
