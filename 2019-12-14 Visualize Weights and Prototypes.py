#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


from classy import *


# In[26]:


def get_square(arr,index,shape,locations=None):
    import json
    
    if locations is None:
        with open('locations.json') as json_file:
            locations = json.load(json_file)        
    
    try:
        location=locations[index]
    except IndexError:
        print("locations.json file probably corrupt.")
        raise 
        
    c,r=location
    c1=int(c-shape[1]/2)
    c2=int(c+shape[1]/2)
    r1=int(r-shape[0]/2)
    r2=int(r+shape[0]/2)

    c2=c2+(shape[1]-(c2-c1))
    r2=r2+(shape[0]-(r2-r1))

    square=arr[r1:r2,c1:c2,:]
    
    return square


# In[27]:


images=image.load_images('/Users/bblais/Desktop/ai373/images/board images/squares')
shape=images.data[0].shape[:2]
data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

classifier=NaiveBayes()
timeit(reset=True)
classifier.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# ## prototypes for naive bayes

# In[28]:


classifier.means


# In[29]:


classifier.means.shape


# In[30]:


target='red'
target_index=images['target_names'].index(target)
shape_3d=list(shape)+[3]
imshow(classifier.means[target_index,:].reshape(shape_3d)/255)
title(target)


# In[32]:


target='black'
target_index=images['target_names'].index(target)
shape_3d=list(shape)+[3]
imshow(classifier.means[target_index,:].reshape(shape_3d)/255)
title(target)


# ## Perceptron

# In[34]:


images=image.load_images('/Users/bblais/Desktop/ai373/images/board images/squares')
shape=images.data[0].shape[:2]
data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

classifier=Perceptron()
timeit(reset=True)
classifier.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[35]:


classifier.weights


# In[36]:


classifier.weights.shape


# In[40]:


target='red'
target_index=images['target_names'].index(target)
shape_3d=list(shape)+[3]
im=classifier.weights[target_index,:].reshape(shape_3d)
im=im-im.min()
im=im/im.max()
imshow(im)
title(target)


# In[41]:


target='black'
target_index=images['target_names'].index(target)
shape_3d=list(shape)+[3]
im=classifier.weights[target_index,:].reshape(shape_3d)
im=im-im.min()
im=im/im.max()
imshow(im)
title(target)


# ## Backprop

# In[63]:


images=image.load_images('/Users/bblais/Desktop/ai373/images/board images/squares')
shape=images.data[0].shape[:2]
data_train=data=image.images_to_vectors(images,verbose=True)  # train on all of them

classifier=BackProp()
timeit(reset=True)
classifier.fit(data_train.vectors,data_train.targets)
print("Training time: ",timeit())


# In[65]:


classifier.weights[0].shape  # input units


# In[66]:


classifier.weights[1].shape  # hidden units


# ### what does it mean to visualize these?

# In[80]:


# can't specify target easily
shape_3d=list(shape)+[3]
im=classifier.weights[0][:,2].reshape(shape_3d)
im=im-im.min()
im=im/im.max()
imshow(im)


# In[ ]:




