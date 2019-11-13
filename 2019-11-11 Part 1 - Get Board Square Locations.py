#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'qt5')


# In[2]:


from pylab import *


# In[3]:


def onkey(event):
    global locations
    from pylab import close
    import os
    import json
    global fig
    
    if event.key=='escape':
        print("locations=",array(locations).__repr__())
        with open('locations.json', 'w') as outfile:
            json.dump(locations, outfile)
    
        close(fig)
        
def onclick(event):
    from pylab import plot,show,close
    global ix, iy
    global locations,fig,ax
    
    ix, iy = event.xdata, event.ydata
    global coords
    coords = [int(ix), int(iy)]
    print(coords)
    
    locations.append(coords)
    
    ax.plot(ix,iy,'go')
    fig.canvas.draw()
    show()
    return coords

def get_square_locations(filefilter):
    from pylab import imread,imsave,imshow,figure,show
    from glob import glob
    global locations,fig,ax
    locations=[]
    stop=False
    
    fnames=glob(filefilter)
    
    fig=figure()
    ax=subplot(1,1,1)
    arr=imread(fnames[0])
    imshow(arr)
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    cid2 = fig.canvas.mpl_connect('key_press_event', onkey)
    show()
    


# In[5]:


get_square_locations('/Users/bblais/Desktop/ai373/images/board images/*.jpg')


# In[ ]:




