# Idea: The monster comes for the knight
# We will use BFS algorithm
# Go from bottom right to top left, and we can only go up and go left
# The monster start from 0 health and it can be greater 0 (if it does, set it be 0)
# The result will be 1 - visited[0][0] because we need the health of the knight is greater than 0

def save_the_pricess(board):
    m = len(board)
    n = len(board[0])

    # matrix that store the cost to go from bottom to all locations
    visited_matrix = [[-1e9 for _ in range(n)] for _ in range(m)]
    
    queue = []
    queue.append([m-1, n-1])
    
    visited_matrix[-1][-1] = board[-1][-1] if board[-1][-1] < 0 else 0
    while(len(queue) > 0):
        x, y = queue.pop(0)
        
        # Go up if possible
        if (x-1 >= 0):
            tmp = visited_matrix[x][y] + board[x-1][y] if visited_matrix[x][y] + board[x-1][y] < 0 else 0
            if tmp > visited_matrix[x-1][y]:
                visited_matrix[x-1][y] = tmp
                queue.append([x-1, y])
            
        # Go left if possible
        if (y-1 >= 0):
            tmp = visited_matrix[x][y] + board[x][y-1] if visited_matrix[x][y] + board[x][y-1] < 0 else 0
            if tmp > visited_matrix[x][y-1]:
                visited_matrix[x][y-1] = tmp
                queue.append([x, y-1])
    print(visited_matrix)

    return 1 - visited_matrix[0][0]

# board = [[-2, -3, 3],
#          [-5, -10, 1],
#          [10, 30, -5]]
board = [[-3, 5]]

print(save_the_pricess(board))