
### Fucntion displays board when passed a list 
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
    
    p1mark = 'null'
    p2mark = 'null'

    markers = ['X','O']
    
    while p1mark not in markers:
        
        p1mark = input("Player 1, do you want to be X or O? ")
        
        if p1mark not in markers:
            print('Sorry, that was not a choice!')
        
        if p1mark in markers: 
            if p1mark == markers[0]:
                p2mark = markers[1]
            elif p1mark == markers[1]:
                p2mark = markers[0]
            print(f"Player 1 is {p1mark}, and Player 2 is {p2mark}")

### 