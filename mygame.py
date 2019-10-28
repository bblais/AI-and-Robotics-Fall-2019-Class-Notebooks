from Game import *
from Game.minimax import *

def initial_state():
    state=Board(3,3)
    state.pieces=['.','X','O']
    
        
    return state


# In[3]:


def update_state(state,player,move):
    new_state=state
    new_state[move]=player
    return new_state


# In[4]:


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
    
    
    


# In[5]:


def valid_moves(state,player):

    moves=[]  # no valid moves
    for i in range(9):
        if state[i]==0:
            moves.append(i)
    
    return moves


# In[6]:


def show_state(state):
    print(state[0],'|',state[1],'|',state[2])
    print("--+---+---")
    print(state[3],'|',state[4],'|',state[5])
    print("--+---+---")
    print(state[6],'|',state[7],'|',state[8])


# Move Functions for the Agents

# In[7]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)


# In[8]:


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


# In[9]:


human_agent=Agent(get_human_move)
random_agent=Agent(random_move)


# In[10]:


def minimax_move(state,player):

    values,moves=minimax_values(state,player)
    return top_choice(moves,values)


minimax_agent=Agent(minimax_move)


# In[11]:


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


# In[12]:


def skittles_after(status,player,info):
    S=info.S
    last_state=info.last_state
    last_action=info.last_action
    
    if status=='lose':
        S[last_state][last_action]-=1
        if S[last_state][last_action]<0:
            S[last_state][last_action]=0
            


# In[13]:


skittles_agent1=Agent(skittles_move)
skittles_agent1.S=LoadTable("TTT Skittles 1.json")
skittles_agent1.post=skittles_after


skittles_agent2=Agent(skittles_move)
skittles_agent2.S=LoadTable("TTT Skittles 2.json")
skittles_agent2.post=skittles_after


# ### Running the Game - Random vs Skittles 2

# In[14]:
