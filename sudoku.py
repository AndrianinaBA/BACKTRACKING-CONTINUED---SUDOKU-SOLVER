grid = [[0,3,1,4,0,5,0,7,0],
        [6,2,0,0,8,0,4,0,0],
        [7,0,0,0,0,1,0,0,9],
        [2,0,6,0,0,3,8,0,0],
        [0,0,0,0,0,0,2,0,3],
        [0,1,3,6,0,0,9,5,0],
        [0,0,8,0,4,7,0,0,0],
        [0,0,0,9,0,0,0,0,6],
        [0,0,9,0,5,0,3,8,2]]

def is_possible(guess:int ,row,col):
    global grid
    for c in range(9):
        if grid[row][c] == guess :
            return False
    for r in range(9):
        if grid[r][col] == guess :
            return False
    x = (row//3)*3
    y = (col//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == guess :
                return False
    return True

print(is_possible(1,0,2))
