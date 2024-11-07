import copy

def solve(board):
    print("Solving board")
    copy_board = copy.deepcopy(board)
    
    # add in backtracking logic here that will solve the board using the 2d array
    return copy_board



def is_safe_helper(copy_board, row, col):
    for i in range(row):
        if copy_board[i][col] == "Q":
            return False
    for i in range(col):
        if copy_board[row][i] == 'Q':
            return False    
    return True