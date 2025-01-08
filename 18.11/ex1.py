def find_max_sub_array(arr):
    idx_left = 0
    result_left = 0
    result_right = 0   
    max_sum = -1e9

    tmp_right = 0
    curr_sum = 0
    negative_sum = 0        
    i = 0
    while (i < len(arr)):
        # If arr[i] > 0, just add it to curr_sum, and then check if it is the largest so far
        if arr[i] >= 0:
            curr_sum += arr[i]
            
            if (curr_sum > max_sum):
                max_sum = curr_sum
                result_left = idx_left
                result_right = i
            i+=1
        # if arr[i] < 0
        else:
            # find the consercutive negative numbers
            tmp_right = i - 1
            while(i < len(arr) and arr[i] < 0):
                negative_sum += arr[i]
                i+=1
            # If the curr_sum plus the negative_sum is < 0, we can drop all of them and start from next index
            # check if the current sum if it is the largest so far
            if (curr_sum + negative_sum < 0):
                if (curr_sum > max_sum):
                    max_sum = curr_sum
                    result_left = idx_left
                    result_right = tmp_right
            
            # reset the current sum and the idx_left
                curr_sum = 0
                idx_left = i
            # if the curr_sum + negative sum >= 0, keep them, update curr_sum
            else:
                curr_sum += negative_sum
            # reset negative_sum
            negative_sum = 0
            
    # all numbers are negative
    if result_right == -1:
        return max(arr)
    return arr[result_left: result_right+1], max_sum

#arr = [4, 1, 1, -1, -2, 1, -1, 5, -1, -5, 6]
#arr = [13, -2, 4, -5, 9, -10, 1, -2 , 4]
arr = [-1, -2]
print(find_max_sub_array(arr))            