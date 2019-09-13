#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('gui', 'tk')


# In[5]:


from turtle import *


# In[3]:


forward(50)


# In[4]:


forward(50)


# In[5]:


right(90)


# In[6]:


forward(50)


# In[7]:


reset()

forward(50)
right(90)

forward(50)
right(90)


# In[ ]:





# In[ ]:





# In[12]:


reset()

this_is_the_size_of_the_square=200

forward(this_is_the_size_of_the_square)
right(90)

forward(this_is_the_size_of_the_square)
right(90)

forward(this_is_the_size_of_the_square)
right(90)

forward(this_is_the_size_of_the_square)
right(90)


# In[13]:


reset()

this_is_the_size_of_the_square=200

print("Start!")
for i in range(4):  # this repeats 4 times

    forward(this_is_the_size_of_the_square)
    right(90)

    print("Here")
    
print("End.")


# In[14]:


def square(size):
    for i in range(4):  # this repeats 4 times
        forward(size)
        right(90)    


# In[15]:


reset()
square(50)


# In[ ]:





# In[16]:


reset()
square(50)

penup()
foward(100)
pendown()

square(50)


# In[17]:


reset()
square(50)

penup()
forward(100)
pendown()

square(50)


# In[23]:


a=5

if a>5:
    print("Big!")
    print("Here")
elif a==5:
    print("Just Right Goldilocks!")
else:
    print("Small!")
    print("There")
    


# In[24]:


a


# In[25]:


a=a+1


# In[26]:


a


# In[27]:


5==5


# In[28]:


5==6


# In[29]:


a=5

if a>2:
    print("Big!")
    print("Here")
elif a==5:
    print("Just Right Goldilocks!")
else:
    print("Small!")
    print("There")
    


# In[6]:


forward(50)


# In[8]:


from numpy.random import randn


# In[10]:


for i in range(100):
    forward(randn()*10)
    right(90)


# In[12]:


reset()
speed('fastest')

for i in range(1000):
    forward(randn()*10)
    right(90)


# In[13]:


reset()
speed('fastest')

while True:
    forward(randn()*10)
    right(90)


# In[14]:


def blah(a):
    print(a)
    a=2*a
    print(a)
    
    return 5*a


# In[15]:


a=7
blah(9)


# In[16]:


a


# In[17]:


a=7
blah(a)


# In[18]:


a


# In[19]:


a=[4,5,6]


# In[20]:


a[1]


# In[21]:


def func(bob):
    bob[1]=100


# In[22]:


func(a)


# In[23]:


a


# In[ ]:




