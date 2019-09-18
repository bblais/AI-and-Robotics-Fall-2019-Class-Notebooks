#!/usr/bin/env python
# coding: utf-8

# ## TTT (Tic Tac Toe) Implementation with Board

# * what is the state: list of 9 #'s, values 0, 1, 2
# * what is a move: position, single # from 0-8
# * what is a list of moves: [2,3,6,8]

# In[1]:


from Game import *


# In[2]:


def initial_state():
    state=Board(3,3)
    return state


# In[3]:


b=Board(3,5)
b


# In[4]:


b[4]=1
b


# In[5]:


b[2,3]=2
b


# In[6]:


b.index_from_rc(2,3)


# In[7]:


b.rc_from_index(13)


# In[8]:


row,col=b.rc_from_index(13)
row,col


# In[9]:


start=4
end=7
move=[start,end]


# In[10]:


move


# In[11]:


start,end=move


# In[12]:


start


# In[13]:


end


# In[14]:


state=Board(4,4)
state


# In[15]:


state[0]=1
state[1]=1

state[15]=2
state[14]=2
state


# In[16]:


state.show_locations()


# In[17]:


moves=[]

if state[0]==1 and state[4]==0:
    moves.append([0,4])
if state[1]==1 and state[5]==0:
    moves.append([0,5])
    
moves
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# example nested loop

# In[18]:


for i in range(3,6):
    for j in range(2,5):
        print(i,j)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


# test
a=initial_state()


# In[20]:


a


# In[21]:


a[5]=2


# In[22]:


a


# In[23]:


a[2,1]=1


# In[24]:


a


# In[25]:


# this one won't work for TTT
# def get_stupid_move(state,player):
#     move=1
#     return move


# In[55]:


def get_human_move(state,player):
    move=input('What square do you want to move to?')
    move=int(move)
    return move


# In[56]:


state=initial_state()
state


# In[57]:


get_human_move(state,1)


# In[ ]:





# In[27]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player
    return new_state


# In[28]:


# quick diversion about lists


# In[29]:


S=[4,6,2,5,3]


# In[30]:


S[3]


# In[31]:


S[3]=9


# In[32]:


S


# In[33]:


S.append(10)


# In[34]:


S


# In[35]:


S=S + [7]


# In[36]:


S


# In[37]:


# test
update_state([0,0,0,0,0,0,0,0,0],2,4)


# In[38]:


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
    
    
    


# In[39]:


def valid_moves(state,player):

    moves=[]  # no valid moves
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves


# In[40]:


# test
valid_moves([0,0,0,0,0,0,0,0,0],1)


# In[41]:


valid_moves([1,0,0,0,0,0,0,0,2],1)


# In[42]:


valid_moves([1,0,0,1,0,0,0,0,2],1)


# In[43]:


def show_state(state):
    print(state[0],'|',state[1],'|',state[2])
    print("--+---+---")
    print(state[3],'|',state[4],'|',state[5])
    print("--+---+---")
    print(state[6],'|',state[7],'|',state[8])


# In[44]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[45]:


show_state(initial_state())


# In[51]:


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


# In[52]:



human_agent=Agent(get_human_move)
random_agent=Agent(random_move)


# In[53]:


g=Game()
g.run(random_agent,human_agent)


# In[ ]:




