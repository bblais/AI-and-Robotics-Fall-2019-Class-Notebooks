#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


def make_training_squares(filefilter,shape,locations=None):
    from glob import glob
    import os
    import json
    
    if locations is None:
        with open('locations.json') as json_file:
            locations = json.load(json_file)        
    
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
    base,name=os.path.split(fnames[0])
    newdirname=base+"/squares"
    if not os.path.exists(newdirname):
        os.mkdir(newdirname)
    
    for fname in fnames:
        arr=array(imread(fname))
        base,name=os.path.split(fname)
        base,ext=os.path.splitext(name)
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
            print(newdirname+"/"+newfname)
            imsave(newdirname+"/"+newfname,square)


# In[3]:


make_training_squares('/Users/bblais/Desktop/ai373/images/board images/*.jpg',(40,40))

