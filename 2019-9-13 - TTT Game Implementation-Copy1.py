#!/usr/bin/env python
# coding: utf-8

# ## TTT (Tic Tac Toe) Implementation

# * what is the state: list of 9 #'s, values 0, 1, 2
# * what is a move: position, single # from 0-8
# * what is a list of moves: [2,3,6,8]

# In[37]:


from Game import *


# In[38]:


def initial_state():
    state=[ 0,0,0,0,0,0,0,0,0 ]
    return state


# In[39]:


# test
a=initial_state()


# In[40]:


a


# In[41]:


# this one won't work for TTT
# def get_stupid_move(state,player):
#     move=1
#     return move


# In[42]:


def get_human_move(state,player):
    move=input('What square do you want to move to?')
    move=int(move)
    return move


# In[43]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player
    return new_state


# In[44]:


# quick diversion about lists


# In[45]:


S=[4,6,2,5,3]


# In[46]:


S[3]


# In[47]:


S[3]=9


# In[48]:


S


# In[49]:


S.append(10)


# In[50]:


S


# In[51]:


S=S + [7]


# In[52]:


S


# In[53]:


# test
update_state([0,0,0,0,0,0,0,0,0],2,4)


# In[54]:


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
    
    
    


# In[55]:


def valid_moves(state,player):

    moves=[]  # no valid moves
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves


# In[56]:


# test
valid_moves([0,0,0,0,0,0,0,0,0],1)


# In[57]:


valid_moves([1,0,0,0,0,0,0,0,2],1)


# In[58]:


valid_moves([1,0,0,1,0,0,0,0,2],1)


# In[59]:


def show_state(state):
    print(state[0],'|',state[1],'|',state[2])
    print("--+---+---")
    print(state[3],'|',state[4],'|',state[5])
    print("--+---+---")
    print(state[6],'|',state[7],'|',state[8])


# In[60]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[61]:


show_state(initial_state())


# In[67]:


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


# In[68]:



human_agent=Agent(get_human_move)
random_agent=Agent(random_move)


# In[69]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:




