import pylab as py

class Turtle(object):
    
    def __init__(self):
        self.reset()

    def reset(self,figsize=(10,10)):
        self.x=0
        self.y=0
        self.angle=0
        
        self.color='k'
        
        self.pen='down'
        self._reset=True   
        self.fig=None
        self.ax=None
        self.figsize=figsize
        self.data=[]
        
    def clear(self):
        fig=py.figure(figsize=self.figsize)
        ax=fig.gca()

        self.fig=fig
        self.ax=ax

        ax.clear()
        ax.axis('equal')
        ax.axis([-100,100,-100,100])

        self.data=[]
        
    def forward(self,length):
        if self._reset:
            self.clear()
            self._reset=False

        fig=self.fig
        ax=self.ax
        
        dx=length*py.cos(py.radians(self.angle))
        dy=length*py.sin(py.radians(self.angle))
        
        if self.pen=='down':
            ax.plot([self.x,self.x+dx],[self.y,self.y+dy],
                         color=self.color,
                         linestyle='-')
            self.data.append([
                [self.x,self.x+dx],[self.y,self.y+dy],self.color,
            ])
        else:
            self.data.append([
                [self.x,self.x+dx],[self.y,self.y+dy],None,
            ])
            
            
        self.x+=dx
        self.y+=dy
        
    def goto(self,x,y):
        if self._reset:
            self.clear()
            self._reset=False

        fig=self.fig
        ax=self.ax
        
        if self.pen=='down':
            ax.plot([self.x,x],[self.y,y],
                         color=self.color,
                         linestyle='-')
            self.data.append([
                [self.x,x],[self.y,y],self.color,
            ])
        else:
            self.data.append([
                [self.x,x],[self.y,y],None,
            ])
            
            
        self.x=x
        self.y=y
        
        
    def backward(self,length):
        self.forward(-self.length)
        
    def right(self,angle):
        self.angle+=angle
        self.angle=self.angle % 360
        
    def left(self,angle):
        self.right(-angle)
        
        
_t=Turtle()

def forward(length):
    global _t
    _t.forward(length)
    
def backward(length):
    forward(-length)
    
def right(angle):
    global _t
    _t.right(angle)
    
def left(angle):
    right(-angle)

def penup():
    global _t
    _t.pen='up'
    
def pendown():
    global _t
    _t.pen='down'    
    
def pencolor(color):
    global _t
    _t.color=color  

def reset(*args,**kwargs):
    global _t
    _t.reset(*args,**kwargs)
    
def speed(arg):
    pass

def goto(x,y):
    global _t
    _t.goto(x,y)
    
def animate(delay=0.05,figsize=(5,5)):
    global _t
    from IPython.display import clear_output
    import time

    for i in range(len(_t.data)+1):
        clear_output(wait=True)
        fig=py.figure(figsize=figsize)
        ax = fig.add_subplot(111)
        ax.clear()
        ax.axis('equal')
        ax.axis([-100,100,-100,100])
        for x,y,c in _t.data[:i]:
            if c is not None:
                ax.plot(x,y,color=c,linestyle='-')
            
        x,y,c = _t.data[i-1]            
        ax.plot([x[1]],[y[1]],'go')
        py.show() 
        time.sleep(delay)    
    