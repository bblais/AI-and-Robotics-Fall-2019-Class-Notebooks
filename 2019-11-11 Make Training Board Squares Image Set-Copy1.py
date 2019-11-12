#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('matplotlib', 'tk')


# In[7]:


from pylab import *


# In[8]:


def onkey(event):
    global stop
    
    if event.key=='escape':
        stop=True
        
    
def onclick(event):
    global ix, iy
    global locations
    
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d'%(
        ix, iy))

    global coords
    coords = [ix, iy]

    locations.append(coords)
    
    plot(ix,iy,'go')
    show()
    return coords


# In[9]:


arr=imread('images/test9.jpg')


# In[10]:


fig=figure()
imshow(arr)

for i in range(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', onclick)


show()


# In[11]:


coords


# In[1]:


ls /Users/bblais/Desktop/ai373/images/


# In[14]:


del fig


# In[1]:


get_ipython().run_line_magic('matplotlib', 'tk')


# In[2]:


from pylab import *


# In[3]:


def onkey(event):
    global locations
    import os
    
    if event.key=='escape':
        print("locations=",array(locations).__repr__())
        
    
def onclick(event):
    from pylab import plot,show
    global ix, iy
    global locations
    
    ix, iy = event.xdata, event.ydata
    global coords
    coords = [ix, iy]

    locations.append(coords)
    
    plot(ix,iy,'go')
    show()
    return coords

def get_square_centers(filefilter):
    from pylab import imread,imsave,imshow,figure,show
    from glob import glob
    global locations
    locations=[]
    stop=False
    
    fnames=glob(filefilter)
    
    fig=figure()
    arr=imread(fnames[0])
    imshow(arr)
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    cid2 = fig.canvas.mpl_connect('key_press_event', onkey)
    show()
    


# In[4]:


get_square_centers('/Users/bblais/Desktop/ai373/images/board images/*.jpg')


# In[ ]:





# In[ ]:





# In[4]:





# In[3]:


get_ipython().run_line_magic('pylab', 'inline')


# In[21]:


def make_training_squares(filefilter,shape,locations):
    from glob import glob
    import os
    
    fnames=glob(filefilter)
    arr=array(imread(fnames[0]))
    for location in locations:
        c,r=location
        c1=int(c-shape[1]/2)
        c2=int(c+shape[1]/2)
        r1=int(r-shape[0]/2)
        r2=int(r+shape[0]/2)

        c2=c2+(shape[1]-(c2-c1))
        r2=r2+(shape[0]-(r2-r1))

        arr[r1:r2,c1:c2,:]=arr[r1:r2,c1:c2,:]+100
        

    clf()
    imshow(arr)

    for fname in fnames:
        base,ext=os.path.splitext(fname)
        for i,location in enumerate(locations):
            c,r=location
            c1=int(c-shape[1]/2)
            c2=int(c+shape[1]/2)
            r1=int(r-shape[0]/2)
            r2=int(r+shape[0]/2)

            c2=c2+(shape[1]-(c2-c1))
            r2=r2+(shape[0]-(r2-r1))

            square=arr[r1:r2,c1:c2,:]
            
            newfname=base+"_%d" %(i) + ext
            


# In[22]:


make_training_squares('/Users/bblais/Desktop/ai373/images/board images/*.jpg',(40,40),
                            locations= array([[ 89.00649351,  55.91558442],
                                   [145.11038961,  55.91558442],
                                   [202.77272727,  55.13636364],
                                   [263.55194805,  54.35714286],
                                   [267.44805195, 105.00649351],
                                   [207.44805195, 107.34415584],
                                   [141.21428571, 109.68181818],
                                   [ 83.55194805, 108.9025974 ],
                                   [ 78.0974026 , 166.56493506],
                                   [142.77272727, 163.44805195],
                                   [206.66883117, 164.22727273],
                                   [269.78571429, 165.00649351],
                                   [272.9025974 , 221.88961039],
                                   [203.55194805, 225.00649351],
                                   [146.66883117, 225.00649351],
                                   [ 77.31818182, 222.66883117]]))


# In[4]:


a=rand(4,5)


# In[5]:


a


# In[8]:


print(a.__repr__())


# In[ ]:




