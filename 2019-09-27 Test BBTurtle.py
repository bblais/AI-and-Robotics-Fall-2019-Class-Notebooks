#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bbturtle import *


# In[2]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)
    


# In[3]:


square(10)


# In[4]:


reset((8,8))

penup()
goto(-75,0)
pendown()

color='red'
for i in range(10):
    pencolor(color)
    square(10)

    penup()
    forward(15)
    pendown()

    if color=='red':
        color='black'
    else:
        color='red'
    


# In[5]:


animate()


# In[ ]:




