#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'tk')


# In[2]:


from pylab import *


# In[5]:


def onkey(event):
    global locations
    import os
    import json
    
    
    if event.key=='escape':
        print("locations=",array(locations).__repr__())
        with open('locations.json', 'w') as outfile:
            json.dump(locations, outfile)
    
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

def get_square_locations(filefilter):
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
    


# In[6]:


get_square_locations('/Users/bblais/Desktop/ai373/images/board images/*.jpg')


# In[ ]:




