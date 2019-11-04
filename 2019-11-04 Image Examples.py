#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


arr=imread('images/bird.jpg')


# In[3]:


imshow(arr)


# In[4]:


nrows,ncols=arr.shape[0],arr.shape[1]


# In[5]:


nrows,ncols


# In[6]:


start_col=ncols//4
end_col=2*ncols//4
part=arr[:,start_col:end_col,:]


# In[7]:


imshow(part)


# In[8]:


355/4


# In[9]:


355//4


# In[10]:


start_col=2*ncols//4
end_col=3*ncols//4
part=arr[:,start_col:end_col,:]


# In[11]:


imshow(part)


# In[15]:


figure(figsize=(8,16))
for p in range(4):
    start_col=p*ncols//4
    end_col=(p+1)*ncols//4
    part=arr[:,start_col:end_col,:]
    
    subplot(1,4,p+1)
    imshow(part)
    
    gca().set_xticks([])
    gca().set_yticks([])


# In[ ]:




