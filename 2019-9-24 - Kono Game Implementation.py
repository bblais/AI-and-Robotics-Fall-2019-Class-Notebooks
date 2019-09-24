#!/usr/bin/env python
# coding: utf-8

# In[13]:


from Game import *
from Game.minimax import *


# http://www.di.fc.ul.pt/~jpn/gv/kono2.htm
# 
# This game is played on the following 4x4 square board:
# 
# <img src="images/2019-09-24 07.21.03 am.png" width=200>
# 
# 
# * **TURNS** 
#    - At each turn, each player must capture an enemy stone.
#    - A stone is captured by orthogonally jumping with a friendly stone over an adjacent friendly stone, and landing over an enemy stone on the immediate next cell (so all three stones must be in the same orthogonal line).
#    - When there are no captures available, the current player moves a friendly stone to adjacent empty cell.
# * **GOAL** 
#    - Wins the player that stalemates the adversary (i.e., leaves no valid move).
# 
# <img src="images/2019-09-24 07.24.27 am.png" width=600>

# In[2]:


def initial_state():
    state=Board(4,4)
    for row in range(4):
        
        # fill in the black pieces
        for col in range(2):
            state[row,col]=2
            
        # fill in the white pieces
        for col in range(2,4):
            state[row,col]=1
            
    # just to make the printing look nicer
    state.pieces=['.','W','B']
    
    return state


# In[9]:


initial_state()


# In[4]:


def show_state(state):
    print(state)


# In[5]:


def human_move(state,player):
    state.show_locations()
    
    start=input("Which piece do you want to move? (enter the start location)")
    start=int(start)
    
    end=input("Where do you want to move it? (enter the end location)")
    end=int(end)
    
    # a move is a short 2-list of start and end locations
    move=[start,end]
    return move


# In[7]:


def win_status(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    if not valid_moves(state,other_player):
        return 'win'
    


# In[8]:


def update_state(state,player,move):
    start=move[0]
    end=move[1]
    
    new_state=state
    new_state[start]=0
    new_state[end]=player
    
    return new_state


# valid_moves() is the most complex function here.
# 
#      0  1  2  3 
#      4  5  6  7 
#      8  9 10 11 
#     12 13 14 15 
# 

# In[11]:


def valid_moves(state,player):
    if player==1:
        other_player=2
    else:
        other_player=1
    
    moves=[]
    # check horizontal moves
    for start in [0,4,8,12,1,5,9,13]:
        middle=start+1
        end=start+2

        # jumping right
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
            
        start,end=end,start  # swap the end and start squares
        # jumping left
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
            
    # check vertical moves
    for start in [0,1,2,3,4,5,6,7]:
        middle=start+4
        end=start+8

        # jumping down
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])
            
        start,end=end,start  # swap the end and start squares
        # jumping up
        if state[start]==player and state[middle]==player and state[end]==other_player:
            moves.append([start,end])

    return moves


# In[12]:


valid_moves(initial_state(),1)


# In[14]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[16]:


human_agent=Agent(human_move)
random_agent=Agent(random_move)


# In[17]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[23]:


g=Game()
g.run(minimax_agent,random_agent)


# ## With max depth

# In[25]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,maxdepth=2)
    return top_choice(moves,values)

def heuristic(state,player):
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
        
    number_white_pieces=0
    number_black_pieces=0
    for i in range(16):
        if state[i]==1:
            number_white_pieces=number_white_pieces+1
        if state[i]==2:
            number_black_pieces=number_black_pieces+1
            
    total_pieces=number_white_pieces+number_black_pieces
    
    value=(number_white_pieces-number_black_pieces)/total_pieces
    
    if player==2:
        value=-value
    
    return value

minimax_agent=Agent(minimax_move)


# In[26]:


g=Game()
g.run(minimax_agent,random_agent)


# In[ ]:




