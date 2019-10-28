from mygame import *
from Robot373 import *

def make_move(move):
    print("this is where I make a move!",move)

def read_state():
    # do some amazing things here to read the state
    print("enter the current state like:  0 0 1 0 0 2 0 0 0")
    x=input()
    b=Board(3,3)
    b.board=[int(i) for i in x.split()]

    return b

def do_happy_dance():
    print("Yay! I won!")

def do_sad_dance():
    print("Yay! You won!")

player=1
while True:

    x=input("wait for my turn")

    state=read_state()  # read it from the world
    show_state(state)

    if player==1:
        S=LoadTable("TTT Skittles 1.json")
    else:
        S=LoadTable("TTT Skittles 2.json")

    move=weighted_choice(S[state])

    make_move(move)  # act in the world

    # this is the virtual world
    new_state=update_state(state,player,move)
    if win_status(new_state,player)=='win':
        do_happy_dance()
    if win_status(new_state,player)=='lose':
        do_sad_dance()
