#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[8]:


state=Board(6,6)
state


# In[9]:


state.show_locations()


# In[31]:


state=initial_state()
state[2]=1
state


# In[34]:


move=16
start_row,start_col=state.rc_from_index(move)
print(start_row,start_col)

for row in range(3,6):
    for col in range(4,6):
        state[row,col]=5
state


# In[ ]:





# In[ ]:





# In[29]:


moves=[]

for i in range(36):
    
    if i<6:
        continue 
        
    if state[i]==1 and state[i-6]==0:
        moves.append( [i , i-6  ])
    
moves


# In[28]:


move=[2.3]


# In[30]:


if not move in valid_moves(state,player):
    print("Not!")


# In[ ]:





# In[ ]:





# In[19]:


def initial_state(N=6):
    state=Board(N,N)
    for column in range(N):
        state[N-1,column]=1
    return state


# In[15]:


initial_state()


# In[1]:


def cool_function(bob,sally):
    
    value=bob+sally
    
    return value


# In[2]:


cool_function(9,8)


# In[3]:


a=cool_function(9,8)


# In[4]:


a


# In[5]:


from math import sin


# In[6]:


y=sin(3.1415)


# In[7]:


y


# In[8]:


def quadratic(x,a,b,c):
    return a*x*x + b*x + c


# In[9]:


y=quadratic(5.6,2,6,8)


# In[10]:


y


# In[11]:


# maxdepth example with heuristic 


# In[ ]:




