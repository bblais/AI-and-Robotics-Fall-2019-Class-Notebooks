#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[10]:


plot(rand(100))
xlabel('this')
ylabel('that')


# In[ ]:





# In[2]:


arr=imread('images/test9.jpg')


# In[3]:


imshow(arr)


# In[4]:


arr.shape


# In[13]:


arr


# In[8]:


arr.shape


# In[19]:


L=[3,5,2,3,45,6,3,2,5]
M=[3,5,2,3,45,6,3,2,5,8,9,2]


# In[15]:


L


# In[16]:


L[4]


# In[17]:


L[4:7]


# In[20]:


L[4:],M[4:]


# In[31]:


L[:4]


# In[32]:


L[:]  # beginning to end


# In[21]:


L[7:10]


# In[22]:


L[7:12]


# In[ ]:





# In[23]:


L[12]


# In[26]:


arr_patch=arr[3:8,100:105,2]
arr_patch


# In[29]:


imshow(arr_patch,cmap=cm.gray)
colorbar()


# In[39]:


figure(figsize=(16,8))
blue=arr[:,:,2]
subplot(1,2,1)
imshow(blue,cmap=cm.gray)
colorbar()

subplot(1,2,2)
imshow(arr)


# In[5]:


figure(figsize=(16,8))
red=arr[:,:,0]
subplot(1,2,1)
#imshow(red,cmap=cm.gray)
imshow(red)
colorbar()

subplot(1,2,2)
imshow(arr)


# In[40]:


figure(figsize=(16,8))
green=arr[:,:,1]
subplot(1,2,1)
imshow(green,cmap=cm.gray)
colorbar()

subplot(1,2,2)
imshow(arr)


# In[41]:


get_ipython().run_line_magic('pylab', 'inline')


# In[46]:


pwd


# In[42]:


arr=imread('images/bird.jpg')


# In[43]:


imshow(arr)


# In[44]:


arr.shape


# In[50]:


red=arr[:,:,0]
green=arr[:,:,1]
blue=arr[:,:,2]

figure(figsize=(16,8))
subplot(1,2,1)
imshow(green/255,cmap=cm.gray)
colorbar()

subplot(1,2,2)
imshow(arr)


# In[ ]:




