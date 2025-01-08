# Check if placing a queen on this location is valid or not
def isValid(row, col, board, n):
    # check column
    for i in range(n):
        if board[row][i] == 'Q':
            return False
    # check row
    for i in range(n):
        if board[i][col] == 'Q':
            return False
    # check forward diagonal
    i = row
    j = col
    while (i >= 0 and j >= 0):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while (i < n and j < n):
        if board[i][j] == 'Q':
            return False
        i += 1
        j += 1
    # check backward diagonal
    i = row
    j = col
    while (i >= 0 and j < n):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    i = row
    j = col
    while (i < n and j >= 0):
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    return True

def backtracking(col, n, board, result):
    # if col >=n then if have one result, save it and return
    if (col >= n):
        tmp = []
        for i in range(n):
            tmp_row = ""
            for j in range(n):
                tmp_row += board[i][j]
            tmp.append(tmp_row)
        result.append(tmp)  
        return
    
    # Loop through the row
    for i in range(n):
        # Check valid
        if isValid(i, col, board, n):
            # set the value to Q
            board[i][col] = 'Q'
            # go to next column
            backtracking(col+1, n, board, result)
            # backtracking by setting the value to '.'
            board[i][col] = '.'

def NQueen(n):
    result = []
    
    # create a board
    board = [["." for i in range(n)] for i in range(n)]
    
    # call the backtrack function starting from column 0
    backtracking(0, n, board, result)
    
    return result

print(NQueen(4))