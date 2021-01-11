
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
    if position in range(1,9):
        board[position] = marker
    else:
        print("Sorry that is not a valid position!")
        position = input("Please choose a position for your marker (1-9): ")