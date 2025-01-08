# Idea: at index i, we can jump maximum T[i] steps,
# -> So we find the index in range [i+1, i + T[i]] that i + T[index] is max
# -> Do that until we reach the end
# Be careful with T[i] = 0, never come here


def find_mininum_steps(arr):
    l_arr = len(arr)
    # Start at index 0
    idx = 0
    
    step_count = 0
    while(idx < l_arr):
        # If we can't pass through the 0 case, print error and return
        # This case will not appear in the test cases because the 
        # exercise assume that the final index is always reachable
        if arr[idx] == 0:
            print("This array can't reach to the end")
            return -1
        # Start from the idx + 1 and stop at idx + T[i]
        start = idx + 1
        stop = idx + arr[idx]
        
        # stop >= l_arr-1 means we find the way to the end,
        # stop here and return step_count + 1
        if stop >= l_arr-1:
            return step_count + 1
        
        # Find the maximum of idx + T[idx]
        max = (idx + 1) + arr[idx+1]
        idx = idx + 1
        for i in range(start+1, stop+1):
            # Step over the 0 case
            if arr[i] == 0:
                continue
            
            if max < i + arr[i]:
                max = i + arr[i]
                idx = i
        # Increase counter
        step_count += 1
    return step_count

arr = [0]
print(find_mininum_steps(arr))


