#!/usr/bin/env python
# coding: utf-8

# ## Nim Skittles Agent

# In[3]:


from Game import *
from Game.minimax import *


# In[4]:


def initial_state(size=21):
    state=size
    return state


# In[5]:


def update_state(state,player,move):
    new_state=state-move
    return new_state


# In[6]:


def win_status(state,player):
    # this is called after the state is updated
    if state==1:
        return 'win'
    
    if state==0:
        return 'lose'
    


# In[7]:


def valid_moves(state,player):
    
    if state==1:
        moves=[ 1 ]
    elif state==2:
        moves=[1,2]
    else:
        moves=[1,2,3]
    
    
    return moves


# In[8]:


def show_state(state):
    print("There are ",state,"number of sticks")


# ## Agents

# In[9]:


def human_move(state,player):
    move=input('How many sticks do you take?')
    move=int(move)
    return move


human_agent=Agent(human_move)


# In[10]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[11]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player,display=False)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[ ]:





# In[12]:


def skittles_move(state,player,info):

    S=info.S
    last_state=info.last_state
    last_action=info.last_action

    
    if not state in S:  # if we haven't seen this state before
        S[state]=Table()
        for action in valid_moves(state,player):
            S[state][action]=2
       
    move=weighted_choice(S[state])
    
    # if there are no weights at all for a state, then the move will be None
    
    if move is None:
        
        if last_state:
            S[last_state][last_action]-=1
            if S[last_state][last_action]<0:
                S[last_state][last_action]=0
            
        
        return random_move(state,player)
    
    
    return move


skittles_agent=Agent(skittles_move)


# In[13]:


def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action
    
    if status=='lose':
        S[last_state][last_action]-=1
        if S[last_state][last_action]<0:
            S[last_state][last_action]=0
            
    

    
    


# In[28]:


skittles_agent.S=Table()
skittles_agent.post=skittles_after
SaveTable(skittles_agent.S,'skittles_start_table.json')


# ## Running the Game

# In[29]:


g=Game(size=6)
g.run(random_agent,skittles_agent)


# In[30]:


g=Game(number_of_games=10)
g.display=False
result=g.run(random_agent,skittles_agent)
print(result)
SaveTable(skittles_agent.S,'skittles_after_table.json')


# In[27]:


skittles_agent.S


# In[ ]:




