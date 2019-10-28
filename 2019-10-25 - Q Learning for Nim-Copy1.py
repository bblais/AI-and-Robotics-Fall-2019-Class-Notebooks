#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    return randint(15,25)

def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
        
def show_state(state):
    print ("There are ",state," sticks left.")

def update_state(state,player,move):
    new_state=state-move
    return new_state

def win_status(state,player):

    if state==1:
        return 'win'
    
    elif state==0:
        return 'lose'
    
    else:
        return None


def human_move(state,player):

    move=input('Take 1, 2 or 3 sticks ')
    return move


def perfect_move(state,player):
    move=(state-1)%4
    if move==0:
        move=1
    return move

def random_move(state,player):
    move=random_choice(valid_moves(state,player))
    return move


human_agent=Agent(human_move)
random_agent=Agent(random_move)
perfect_agent=Agent(perfect_move)


# In[3]:


def Q_move(state,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state
    
    alpha=info.alpha  # learning rate
    gamma=info.gamma  # memory 
    epsilon=info.epsilon  # probability of doing random move
    
    if not state in Q:
        Q[state]=Table()
        for action in valid_moves(state,player):
            Q[state][action]=0.0
            
    if random.random()<epsilon:  # random move
        action=random_choice(Q[state])
    else:
        action=top_choice(Q[state])
        
        
    if not last_action is None:  # anything but the first move
        r=0.0
        Q[last_state][last_action]+=alpha*(r + 
            gamma*max([Q[state][a] for a in Q[state]]) -
            Q[last_state][last_action] )
        
    return action

def Q_post(status,player,info):
    Q=info.Q
    last_action=info.last_action
    last_state=info.last_state
    
    alpha=info.alpha  # learning rate
    gamma=info.gamma  # memory 
    epsilon=info.epsilon  # probability of doing random move

    if status=='lose':
        r=-1.0
    elif status=='win':
        r=1.0
    else:
        r=0.0
        
    if not last_action is None:  # anything but the first move
        Q[last_state][last_action]+=alpha*(r -
            Q[last_state][last_action] )
        


# In[4]:


Q_agent=Agent(Q_move)
Q_agent.post=Q_post

Q_agent.Q=Remember(filename='Q_data.json')
Q_agent.alpha=0.3  # learning rate
Q_agent.gamma=0.9  # memory
Q_agent.epsilon=0.1  # chance of making a random move


# In[5]:


g=Game()
g.run(Q_agent,perfect_agent)
g.report()


# In[6]:


Q_agent.Q


# While learning, set epsilon to 0.1

# In[7]:


Q_agent.epsilon=0.1

g=Game(number_of_games=1000)
g.display=False
g.run(Q_agent,perfect_agent)
Remember(Q_agent.Q,filename='Q_data.json')
g.report()


# In[8]:


Q_agent.Q


# When we want to see how good it really is, turn off epsilon (no random moves)

# In[9]:


Q_agent.epsilon=0.0

g=Game(number_of_games=1000)
g.display=False
g.run(Q_agent,perfect_agent)
Remember(Q_agent.Q,filename='Q_data.json')
g.report()


# ## Can a Q-agent play against another?

# In[10]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_post

Q1_agent.Q=Remember(filename='Q1_data.json')
Q1_agent.alpha=0.3  # learning rate
Q1_agent.gamma=0.9  # memory
Q1_agent.epsilon=0.1  # chance of making a random move

Q2_agent=Agent(Q_move)
Q2_agent.post=Q_post

Q2_agent.Q=Remember(filename='Q2_data.json')
Q2_agent.alpha=0.3  # learning rate
Q2_agent.gamma=0.9  # memory
Q2_agent.epsilon=0.1  # chance of making a random move


# In[11]:


Q1_agent.epsilon=0.1
Q2_agent.epsilon=0.1

g=Game(number_of_games=1000)
g.display=False
g.run(Q1_agent,Q2_agent)
Remember(Q1_agent.Q,filename='Q1_data.json')
Remember(Q2_agent.Q,filename='Q2_data.json')
g.report()


# In[12]:


Q1_agent.epsilon=0.0
Q2_agent.epsilon=0.0
Q1_agent.alpha=0.0
Q2_agent.alpha=0.0

g=Game(number_of_games=1000)
g.display=False
g.run(Q1_agent,perfect_agent)
g.report()


# In[13]:


Q1_agent.epsilon=0.0
Q2_agent.epsilon=0.0
Q1_agent.alpha=0.0
Q2_agent.alpha=0.0

g=Game(number_of_games=1000)
g.display=False
g.run(perfect_agent,Q2_agent)
g.report()


# ## things you should do:
# 
# 1. run this more times and explain the structure of the json files
# 2. run this with tic tac toe

# In[ ]:




