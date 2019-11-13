#!/usr/bin/env python
# coding: utf-8

# In[5]:


# use this in a notebook, not on the robot
get_ipython().run_line_magic('pylab', 'inline')


# In[6]:


# use this on the robot
# from pylab import *   


# In[7]:


from Game import *
from classy import *


# In[8]:


def copyfile(src,dst):
    import platform,os
    s=platform.system()
    if s=="Windows":
        copy_command="copy /y"
        src=src.replace('/','\\')
        dst=dst.replace('/','\\')
    else:
        copy_command="cp -f"
        
    cmd=copy_command+" "+src+" "+dst
    print(cmd)
    os.system(cmd)


# In[ ]:





# In[9]:


# get rid of this for the robot, because it has it's own take_picture function
def take_picture(filename='picture.jpg',view=False):
    copyfile('/Users/bblais/Desktop/ai373/images/board images/test9.jpg',filename)
    print("Took picture ",filename)
    
def take_picture(filename='picture.jpg',view=False):  # takes the newest one in the list
    # replace this function with one that actually takes a picture
    from glob import glob
    import os
    fnames=glob('/Users/bblais/Desktop/ai373/images/board images/*.jpg')
    newest = max(fnames, key=os.path.getctime)

    copyfile(newest,filename)
    print("Took picture ",filename)    


# In[10]:


def get_square(arr,index,shape,locations=None):
    import json
    
    if locations is None:
        with open('locations.json') as json_file:
            locations = json.load(json_file)        
    
    location=locations[index]
    c,r=location
    c1=int(c-shape[1]/2)
    c2=int(c+shape[1]/2)
    r1=int(r-shape[0]/2)
    r2=int(r+shape[0]/2)

    c2=c2+(shape[1]-(c2-c1))
    r2=r2+(shape[0]-(r2-r1))

    square=arr[r1:r2,c1:c2,:]
    
    return square


# ### train classifier

# In[11]:


images=image.load_images('/Users/bblais/Desktop/ai373/images/board images/squares')
shape=images.data[0].shape[:2]
data_train=data=image.images_to_vectors(images)  # train on all of them

classifier=kNearestNeighbor()
timeit(reset=True)
classifier.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[12]:


data_train.shape


# In[13]:


def read_state_from_file(filename='current_board.txt'):
    with open(filename) as fid:
        text=fid.read()

    text2=text.strip().split('\n')
    number_of_rows=len(text2)
    number_of_cols=len(text2[0].split())
    
    b=Board(number_of_rows,number_of_cols)
        
    board=[int(v) for v in text.split()]
    b.board=board
    return b
    
def read_state():
    
    take_picture('current_board.jpg')
    arr=imread('current_board.jpg')
    
    # get predictions
    shape=data_train.shape[:2]
    squares=[get_square(arr,i,shape) for i in range(16)]
    test_images=image.array_to_image_struct(squares)
    test_data=image.images_to_vectors(test_images)
    predictions=classifier.predict(test_data.vectors)

    
    
    state=Board(4,4)
    for i in range(16):
        color=data_train.target_names[predictions[i]]
        if color=="white":
            state[i]=0
        elif color=="black":
            state[i]=1
        elif color=="red":
            state[i]=2
        else:
            raise ValueError("You can't get there from here.")

    print("Current state is:")
    print(state)
    
    x=input("""
    Hit return if this is correct, otherwise type a character 
    and the state will be read from current_board.txt.""")
    
    if x:
        state=read_state_from_file()
        
    print("Using")
    print(state)
    
    return state
        


# In[14]:


state=read_state()


# In[ ]:




