#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')


# In[2]:


x=[]
for i in range(20):
    x.append(randint(0,100))
    
x


# In[3]:


import json


# In[6]:


with open('test.json','w') as fid:
    json.dump(x,fid)


# In[7]:


with open('test.json','r') as fid:
    y=json.load(fid)


# In[8]:


y


# In[ ]:




