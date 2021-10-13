# This is a suduku solver
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
    for i in range(0, 9):
        if(board[i][col] != 0):
            arr[board[i][col]-1] += 1
    
    return arr

def check_row(board, row):
    arr = [0,0,0,0,0,0,0,0,0]
    for j in range(0, 9):
        if(board[row][j] != 0):
            arr[board[row][j]-1] += 1
    
    return arr


def check_square(board, row, col):
    arr = [0,0,0,0,0,0,0,0,0]
    row = row - row%3
    col = col - col%3
    for i in range(0, 3):
        for j in range(0,2):
            if(board[row+i][col+j] != 0):
                arr[board[row+i][col+j]-1] += 1
    
    return arr

def check_valid(board, row, col):
    possible = []
    col_nums = check_col(board, col)
    row_nums = check_row(board, row)
    square_nums = check_square(board, row, col)
    for x in range(0, 9):
        if(col_nums[x] == 0 and row_nums[x] ==0 and square_nums[x] ==0):
            possible.append(x+1)
    return possible

def solver(board, i, j):
    possible = []
    if(i==8 and j==9):
        return True
    if(j==9):
        i+=1
        j = 0
    if(board[i][j]>0):
        return solver(board, i, j+1)
    possible = check_valid(board, i, j)
    if(len(possible)>0):
        for x in possible:
            board[i][j] = x
            if(solver(board, i, j+1)):
                return True
        board[i][j] = 0
    return False


if __name__ == '__main__':
    grid = create_grid()
    if(solver(grid, 0, 0)):
        print(grid)


