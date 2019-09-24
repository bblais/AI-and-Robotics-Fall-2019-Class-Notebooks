#!/usr/bin/env python
# coding: utf-8

# ## TTT (Tic Tac Toe) Minimal Implementation

# In[3]:


from Game import *
from Game.minimax import *


# Functions for the Game

# In[4]:


def initial_state():
    state=Board(3,3)
    state.pieces=['.','X','O']
    
    return state


# In[5]:


state=initial_state()
state


# In[6]:


state=Board(3,3)
state


# In[7]:


state.pieces=['.','X','O']


# In[8]:


state


# In[9]:


state[5]=1
state[6]=2
state


# In[10]:


print(state)


# In[11]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player
    return new_state


# In[12]:


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
    
    
    


# In[13]:


def valid_moves(state,player):

    moves=[]  # no valid moves
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves


# In[14]:


def show_state(state):
    print(state[0],'|',state[1],'|',state[2])
    print("--+---+---")
    print(state[3],'|',state[4],'|',state[5])
    print("--+---+---")
    print(state[6],'|',state[7],'|',state[8])


# Move Functions for the Agents

# In[15]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[16]:


def get_human_move(state,player):
    print("Locations:")
    print("    0 | 1 | 2")
    print("    ---------")
    print("    3 | 4 | 5")
    print("    ---------")
    print("    6 | 7 | 8")
    
    while True:
        
        move=input('What square do you want to move to?')
        move=int(move)

        if move in valid_moves(state,player):
            break
        else:
            print("You messed up!")
    
    return move


# In[17]:


human_agent=Agent(get_human_move)
random_agent=Agent(random_move)


# In[18]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[19]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=2)
    return top_choice(moves,values)

def heuristic(state,player):
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
    value=0.0
    if state[4]==player:
        value=value+0.2
        
    if state[4]==other_player:
        value=value-0.2
        
    return value

minimax_agent=Agent(minimax_move)


# In[20]:


minimax_values(state,1)


# In[21]:


minimax_values(state,1,maxdepth=3)


# Running the Game

# In[22]:


g=Game()
g.run(random_agent,minimax_agent)


# In[23]:


g=Game(number_of_games=10)
g.display=False
g.run(random_agent,minimax_agent)


# In[15]:


state=initial_state()
state


# In[16]:


minimax_values(state,1)


# In[22]:


state=initial_state()
state[0]=1
state[1]=2
state


# In[23]:


values,moves=minimax_values(state,1)
values,moves


# In[19]:


state=Board(4,5)


# In[20]:


state.index_from_rc(3,4)


# In[21]:


state.rc_from_index(13)


# In[ ]:




