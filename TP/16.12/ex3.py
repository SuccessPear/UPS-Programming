def getMaxArea(arr):

    n = len(arr)
    s = []
    result = 0

    for i in range(n):
        while s and arr[s[-1]] >= arr[i]:

            # The popped item is to be considered as the 
            # smallest element of the histogram
            tp = s.pop()

            # For the popped item previous smaller element is 
            # just below it in the stack (or current stack top)
            # and next smaller element is i
            width = i if not s else i - s[-1] - 1

            res = max(result, arr[tp] * width)
        s.append(i)

    # For the remaining items in the stack, next smaller does
    # not exist. Previous smaller is the item just below in
    # stack.
    while s:
        tp = s.pop()
        curr = arr[tp] * (n if not s else n - s[-1] - 1)
        res = max(result, curr)

    return res


def find_max_rectangle_area(board: list[list[int]]):
    row = len(board)
    col = len(board[0])
    
    max_area = 0
    temp = [0] * col
    for i in range(row):
        for j in range(col):
            # if board[i][j] = 1 then we add 1 to temp[j]
            if board[i][j] == 1:
                temp[j] += 1
            # if board[i][j] = 0 then we reset the temp[j]
            else:
                temp[j] = 0
        max_temp = getMaxArea(temp)
        max_area = max(max_area, max_temp)
    return max_area

board = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]
print(find_max_rectangle_area(board))