#!/usr/bin/env python
# coding: utf-8

# ## TTT (Tic Tac Toe) Implementation with Board

# * what is the state: list of 9 #'s, values 0, 1, 2
# * what is a move: position, single # from 0-8
# * what is a list of moves: [2,3,6,8]

# In[1]:


from Game import *


# In[30]:


def initial_state():
    state=Board(3,3)
    return state


# In[31]:


# test
a=initial_state()


# In[32]:


a


# In[33]:


a[5]=2


# In[34]:


a


# In[35]:


a[2,1]=1


# In[36]:


a


# In[5]:


# this one won't work for TTT
# def get_stupid_move(state,player):
#     move=1
#     return move


# In[6]:


def get_human_move(state,player):
    move=input('What square do you want to move to?')
    move=int(move)
    return move


# In[7]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player
    return new_state


# In[8]:


# quick diversion about lists


# In[9]:


S=[4,6,2,5,3]


# In[10]:


S[3]


# In[11]:


S[3]=9


# In[12]:


S


# In[13]:


S.append(10)


# In[14]:


S


# In[15]:


S=S + [7]


# In[16]:


S


# In[17]:


# test
update_state([0,0,0,0,0,0,0,0,0],2,4)


# In[18]:


def win_status(state,player):
    # this will be a bit longer
    
#     0 | 1 | 2
#     ---------
#     3 | 4 | 5
#     ---------
#     6 | 7 | 8
    

    if state[0]==player and state[4]==player and state[8]==player:
        return 'win'
    if state[2]==player and state[4]==player and state[6]==player:
        return 'win'
    if state[0]==player and state[1]==player and state[2]==player:
        return 'win'
    if state[3]==player and state[4]==player and state[5]==player:
        return 'win'
    if state[6]==player and state[7]==player and state[8]==player:
        return 'win'
    if state[0]==player and state[3]==player and state[6]==player:
        return 'win'
    if state[1]==player and state[4]==player and state[7]==player:
        return 'win'
    if state[2]==player and state[5]==player and state[8]==player:
        return 'win'
    
    if player==1:
        other_player=2
    else:
        other_player=1
    
    
    if not valid_moves(state,other_player):
        return 'stalemate'
    
    
    


# In[19]:


def valid_moves(state,player):

    moves=[]  # no valid moves
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves


# In[20]:


# test
valid_moves([0,0,0,0,0,0,0,0,0],1)


# In[21]:


valid_moves([1,0,0,0,0,0,0,0,2],1)


# In[22]:


valid_moves([1,0,0,1,0,0,0,0,2],1)


# In[23]:


def show_state(state):
    print(state[0],'|',state[1],'|',state[2])
    print("--+---+---")
    print(state[3],'|',state[4],'|',state[5])
    print("--+---+---")
    print(state[6],'|',state[7],'|',state[8])


# In[24]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[25]:


show_state(initial_state())


# In[26]:


def get_human_move(state,player):
    print("Locations:")
    print("    0 | 1 | 2")
    print("    ---------")
    print("    3 | 4 | 5")
    print("    ---------")
    print("    6 | 7 | 8")
    
    move=input('What square do you want to move to?')
    move=int(move)
    return move


# In[27]:



human_agent=Agent(get_human_move)
random_agent=Agent(random_move)


# In[29]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:




