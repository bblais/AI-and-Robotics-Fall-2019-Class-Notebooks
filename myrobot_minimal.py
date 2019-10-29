from Game import *
from Robot373 import *


def make_move(move):
    print("this is where I make a move!",move)

# hard-code the current state, until we can read it
state=Board(3,3)
state.board=[0,0,1,0,0,0,2,0,0]

move = 2
make_move(move)

