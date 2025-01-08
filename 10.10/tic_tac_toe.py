import random
def lets_play(): 
    board = []
    current_idxes = []
    for i in range(9):
        board.append(0)
        current_idxes.append(i)
    move = 10
    for i in range(9):
        if (move == 10):
            move = 1
        else:
            move = 10
        result = play_one_move(move, board, current_idxes)
        print_board(board, i)
        if result:
            if move == 1:
                print ("X win!!")
            elif move == 10:
                print ("Y win!!")
            return
    print("Tie")
        
def print_board(board, count):
    tmp = []
    for i in range(9):
        if board[i] == 1:
            tmp.append("X")
        elif board[i] == 10:
            tmp.append("O")
        else:
            tmp.append(" ")
    print ("Move {}".format(count+1))
    print ("| {} | {} | {}".format(tmp[0], tmp[1], tmp[2]))
    print ("____________")
    print ("| {} | {} | {}".format(tmp[3], tmp[4], tmp[5]))
    print ("____________")
    print ("| {} | {} | {}".format(tmp[6], tmp[7], tmp[8]))
    print ("End board")

def check_win_condition(board):
    
    win_conditions = []
    win_conditions.append(board[0] + board[3] + board[6])
    win_conditions.append(board[1] + board[4] + board[7])
    win_conditions.append(board[2] + board[5] + board[8])
    win_conditions.append(board[0] + board[1] + board[2])
    win_conditions.append(board[3] + board[4] + board[5])
    win_conditions.append(board[6] + board[7] + board[8])
    win_conditions.append(board[0] + board[4] + board[8])
    win_conditions.append(board[2] + board[4] + board[6])
    
    for i in win_conditions:
        if i == 3 or i == 30:
            return True
    return False

def play_one_move(move, board, current_idxes):
    secure_random = random.SystemRandom()
    idx = secure_random.choice(current_idxes)
    current_idxes.remove(idx)
    board[idx] = move
    if (check_win_condition(board)):
        return True
    else:
        return False

lets_play()