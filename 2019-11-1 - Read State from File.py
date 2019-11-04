#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[5]:


b=Board(4,4)


# In[6]:


def read_state():
    with open('example state.txt') as fid:
        text=fid.read()

    text2=text.strip().split('\n')
    number_of_rows=len(text2)
    number_of_cols=len(text2[0].split())
    
    b=Board(number_of_rows,number_of_cols)
        
    board=[int(v) for v in text.split()]
    b.board=board
    return b


# In[8]:


state=read_state()
print(state,state.shape)


# In[19]:


with open('example state.txt') as fid:
    text=fid.read()

text2=text.strip().split('\n')
text3=text.split('\n')


# In[17]:


text


# In[18]:


text2


# In[20]:


text3


# In[10]:


text.split()


# In[ ]:




