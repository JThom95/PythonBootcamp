
### Fucntion displays board when passed a list 
# Indexes correspond to numpad positions

def display_board(board):
    
    row1 = f' {board[7]} | {board[8]} | {board[9]} '
    row2 = f' {board[4]} | {board[5]} | {board[6]} '
    row3 = f' {board[1]} | {board[2]} | {board[3]} '
    line = '-----------'
    
    rows = f'{row1}\n{line}\n{row2}\n{line}\n{row3}'
    
    print(rows)

### Player Input function 
