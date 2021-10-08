# This is a suduku solver using backtracking


def create_grid():
    grid = [[3,0,6,5,0,8,4,0,0],
            [5,2,0,0,0,0,0,0,0],
            [0,8,7,0,0,0,0,3,1],
            [0,0,3,0,1,0,0,8,0],
            [9,0,0,8,6,3,0,0,5],
            [0,5,0,0,9,0,6,0,0],
            [1,3,0,0,0,0,2,5,0],
            [0,0,0,0,0,0,0,7,4],
            [0,0,5,2,0,6,3,0,0]]
    return grid


def check_col(board, col):
    arr = [0,0,0,0,0,0,0,0,0]
    for i in range(0, 8):
        if(board[i][col] != 0):
            arr[board[i][col]] += 1
    
    return arr

def check_row(board, row):
    arr = [0,0,0,0,0,0,0,0,0]
    for j in range(0, 8):
        if(board[row][j] != 0):
            arr[board[row][j]] += 1
    
    return arr


def check_square(board, row, col):
    arr = [0,0,0,0,0,0,0,0,0]
    if(col%3!=0):
        if(col>3 & col<6):
            col = 3
        elif(col<3):
            col = 0
        elif(col>6):
            col = 6
    
    if(row%3!=0):
        if(row>3 & row<6):
            row = 3
        elif(row<3):
            row = 0
        elif(row>6):
            row = 6
   
    for i in range(0, 2):
        for j in range(0,2):
            if(board[row+i][col+j] != 0):
                arr[board[row+i][col+j]] += 1
    
    return arr

def solver(board, i, j):
    valid_moves = True
    at_end = False
    completed = False
    possible = []
    
    if (board[i][j] == 0):
        col_nums = check_col(board, j)
        row_nums = check_row(board, i)
        square_nums = check_square(board, i, j)
        
    
    
    
    if(valid_moves == False):
        return False
    elif(at_end):
        return board
    else:
        solver(board)


if __name__ == '__main__':
    grid = create_grid()
    print(solver(grid, 0, 0))


