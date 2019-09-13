#!/usr/bin/env python
# coding: utf-8

# ## Nim Implementation

# * how is the state represented: single umber (number of sticks)
# * what is a move: single number (number of sticks to take)
# * what is a list of moves: [1, 2, 3] 
# 
# Reminder: for every function ask *what does it need?* and *what does it return?*

# In[34]:


from Game import *


# In[1]:


def initial_state(size=21):
    state=size
    return state


# In[2]:


# test
print(initial_state(21))

print(initial_state(30))

a=initial_state(35)


# In[3]:


a


# In[4]:


def get_stupid_move(state,player):
    move=1
    return move


# In[5]:


def get_slightly_stupid_move(state,player):
    if state==4:
        move=3
    elif state==3:
        move=2
    elif state==2:
        move=1
    else:
        move=1
    return move


# In[6]:


#
print(get_slightly_stupid_move(6,2))
print(get_slightly_stupid_move(5,2))
print(get_slightly_stupid_move(4,2))
print(get_slightly_stupid_move(3,2))
print(get_slightly_stupid_move(2,2))
print(get_slightly_stupid_move(1,2))


# In[7]:


def get_human_move(state,player):
    move=input('How many sticks do you take?')
    move=int(move)
    return move


# In[8]:


# testing
state=21
player=2


# In[9]:


move=get_stupid_move(state,player)
print(move)


# In[10]:


move=get_human_move(state,player)
print(move)


# In[11]:


move


# In[12]:


move*10


# In[13]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


# In[14]:


# test
update_state(20,1,3)


# In[15]:


def win_status(state,player):
    # this is called after the state is updated
    if state==1:
        return 'win'
    
    if state==0:
        return 'lose'
    


# In[16]:


#test
win_status(3,2)


# In[17]:


win_status(1,1)


# In[18]:


win_status(0,1)


# In[19]:


def valid_moves(state,player):
    
    if state==1:
        moves=[ 1 ]
    elif state==2:
        moves=[1,2]
    else:
        moves=[1,2,3]
    
    
    return moves


# In[20]:


# test
valid_moves(20,1)


# In[21]:


valid_moves(2,1)


# In[28]:


def show_state(state):
    print("There are ",state,"number of sticks")


# In[35]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[30]:


human_agent=Agent(get_human_move)


# In[36]:


stupid_agent=Agent(get_stupid_move)
random_agent=Agent(random_move)


# In[37]:


g=Game()


# In[38]:


g.run(human_agent,random_agent)


# In[ ]:




