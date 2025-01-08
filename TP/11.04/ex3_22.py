# Idea: BFS go from the top left, start with 1 health
# when the knight goes to a monster room, if the current health is not enough, increase the total health a mininum number
# so that the knight can pass the room
# when the knight come to any room, save the mininum init health to come there



def save_the_pricess(board):
    m = len(board)
    n = len(board[0])
    
    # matrix that store the cost to go from start to all locations
    visited_matrix = [[1e9 for _ in range(n)] for _ in range(m)]
    
    init_health_maxtrix = [[1e9 for _ in range(n)] for _ in range(m)]
    queue = []
    queue.append([0, 0])
    
    visited_matrix[0][0] = -board[0][0]
    init_health_maxtrix[0][0] = 1- board[0][0] if board[0][0] < 0 else 1
    while(len(queue) > 0):
        x, y = queue.pop(0)
        
        # Go down if possible
        if (x+1 < m):
            # Update the visit
            if visited_matrix[x][y] - board[x+1][y] < visited_matrix[x+1][y]:
                # Update init and visit
                new_init = init_health_maxtrix[x][y]
                if visited_matrix[x][y] - board[x+1][y] < 0: # this case the knight dies
                    new_init = init_health_maxtrix[x][y] - (visited_matrix[x][y] - board[x+1][y])
                if new_init < init_health_maxtrix[x+1][y]:
                    visited_matrix[x+1][y] = visited_matrix[x][y] - board[x+1][y]
                    init_health_maxtrix[x+1][y] = new_init
                    queue.append([x+1, y])
                # Just update visit
                else:
            
        # Go right if possible
        if (y+1 < n):
            if visited_matrix[x][y] - board[x][y+1] < visited_matrix[x][y+1]:
                visited_matrix[x][y+1] = visited_matrix[x][y] - board[x][y+1]
                queue.append([x, y+1])
    print(visited_matrix)

board = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]

save_the_pricess(board)