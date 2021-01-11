
### Function displays board when passed a list 
# Indexes correspond to numpad positions

def display_board(board):
    row1 = f' {board[7]} | {board[8]} | {board[9]} '
    row2 = f' {board[4]} | {board[5]} | {board[6]} '
    row3 = f' {board[1]} | {board[2]} | {board[3]} '
    line = '-----------'
    
    rows = f'{row1}\n{line}\n{row2}\n{line}\n{row3}'
    
    print(rows)


### Function takes palyer input to choose marker

def player_input(): 
    bool = True
    while bool:
        p1mark = input("Player 1, do you want to be X or O? ")
        if p1mark == 'X' or p1mark == 'O':
            if p1mark == 'X':
                p2mark = 'O'
            else:
                p2mark = 'X'
            print(f"Player 1 is {p1mark}, and Player 2 is {p2mark}")
            bool = False
        else:
            print('Sorry that is not a choice')


### Function Takes in board list obj, a marker, and desired position
# and assigns it to the board 

def place_marker(board, marker, position):
    if position in range(1,10):
        board[position] = marker
    else:
        bool = True
        while bool:
            print("Sorry that is not a valid position!")
            position = int(input("Please choose a position for your marker (1-9): "))
            if position in range(1,10):
                board[position] = marker
                bool = False          


### Function that takes in marker and checks to see if marker has won (returns bool)

def win_check(board, mark):
    
    win = bool
        
    if ((mark == board[1] and mark == board[5] and mark == board [9]) or
        (mark == board[4] and mark == board[5] and mark == board [6]) or
        (mark == board[7] and mark == board[8] and mark == board [9]) or
        (mark == board[7] and mark == board[4] and mark == board [1]) or
        (mark == board[8] and mark == board[5] and mark == board [2]) or 
        (mark == board[9] and mark == board[6] and mark == board [3]) or 
        (mark == board[1] and mark == board[5] and mark == board [9]) or
        (mark == board[7] and mark == board[5] and mark == board [3])):
            win = True
    else:
        win = False
    
    return win    


### Function that randomly decides who goes first (return str)

import random

def choose_first():
    
    designator = random.randint(1,2)

    if designator == 1:
        return 'Player 1 goes first!'
    else:
        return 'Player 2 goes first!'


### Fucntion that checks whether or not a space is open (returns bool)

def space_check(board, position):
    
    openSpace = bool
    
    if board[int(position)] == 'X' or board[int(position)] == 'O':
        openSpace = False
    else:
        openSpace = True
    
    return openSpace


###  Function that checks if the board is full (returns bool)

def full_board_check(board):
       
    boardFull = True 
    
    if boardFull:
        for i in board[1:10]:
            if i != 'X' and i != 'O':
                boardFull = False

    return boardFull

