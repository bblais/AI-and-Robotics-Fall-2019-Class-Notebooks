#!/usr/bin/env python
# coding: utf-8

# ## Nim with Minimax and Table Lookup

# In[1]:


from Game import *
from Game.minimax import *


# In[2]:


def initial_state(size=21):
    state=size
    return state


# In[3]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


# In[4]:


def win_status(state,player):
    # this is called after the state is updated
    if state==1:
        return 'win'
    
    if state==0:
        return 'lose'
    


# In[5]:


def valid_moves(state,player):
    
    if state==1:
        moves=[ 1 ]
    elif state==2:
        moves=[1,2]
    else:
        moves=[1,2,3]
    
    
    return moves


# In[6]:


def show_state(state):
    print("There are ",state,"number of sticks")


# ## Agents

# In[7]:


def human_move(state,player):
    move=input('How many sticks do you take?')
    move=int(move)
    return move


human_agent=Agent(human_move)


# In[8]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[9]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[10]:


def table_move(state,player,info):

    T=info.T
    
    move=weighted_choice(T[state])
    
    # if there are no weights at all for a state, then the move will be None
    
    if move is None:
        return random_move(state,player)
    
    
    return move


table_agent=Agent(table_move)


# In[11]:


table_agent.T=T=Table()

T[1]=Table()
T[1][1]=0

T[2]=Table()
T[2][1]=1
T[2][2]=0

T[3]=Table()
T[3][1]=0
T[3][2]=1
T[3][3]=0

T[4]=Table()
T[4][1]=0
T[4][2]=0
T[4][3]=1

T[5]=Table()
T[5][1]=0
T[5][2]=0
T[5][3]=0

T[6]=Table()
T[6][1]=1
T[6][2]=0
T[6][3]=0


# In[12]:


SaveTable(table_agent.T,'table.json')


# ## Running the Game

# In[16]:


g=Game(size=6)
g.run(random_agent,table_agent)


# In[35]:


g=Game(number_of_games=10)
g.display=False
result=g.run(minimax_agent,random_agent)
print(result)


# In[ ]:





# ## Fill the table with minimax

# In[40]:


table_agent.T=T=Table()

for state in range(1,22):
    T[state]=Table()
    values,moves=minimax_values(state,1,display=False)
    
    for move,value in zip(moves,values):
        T[state][move]=value
        
T


# In[41]:


SaveTable(table_agent.T,'nim_minimax_table.json')


# In[42]:


table_agent=Agent(table_move)
table_agent.T=LoadTable('nim_minimax_table.json')


# In[43]:


g=Game(number_of_games=100)
g.display=False
result=g.run(table_agent,random_agent)
print(result)


# In[ ]:




