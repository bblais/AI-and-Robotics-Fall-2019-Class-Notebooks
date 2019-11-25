#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')


# In[30]:


def read20():
    return list(randint(0,255,20)*1.0)


# In[31]:


def forward1():
    pass


# In[32]:


from classy import *


# In[33]:


data=[]
for i in range(5):
    vec=read20()
    forward1()
    data.append(vec)


# In[35]:


import json

for row in range(5):
    row_filename='row%d.json' % row
    
    with open(row_filename,'w') as fid:
        json.dump(data,fid)
        
    
        
            


# In[37]:


3/2


# In[41]:


D={}
for row in range(5):
    row_filename='row%d.json' % row
    
    with open(row_filename,'r') as fid:
        data=json.load(fid)    
        
    D[str(row)]=data
    
print(D)


# In[42]:


make_dataset(**D,feature_names=[str(_) for _ in range(i)])


# In[ ]:




