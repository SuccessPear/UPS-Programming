def shell_sort(arr: list):
    n = len(arr)
    
    gap = n//2
    while(gap > 0):
        for i in range(gap, len(arr)):
            tmp = arr[i]
            idx = i - gap
            
            while(idx >= 0 and tmp < arr[idx]):
                arr[idx+gap] = arr[idx]
                idx -= gap
            
            arr[idx+gap] = tmp
        gap //= 2
        
arr = [35, 33, 42, 10, 14, 19, 27, 44]
#arr = [2, 5, 8, 7, 9, 14]
shell_sort(arr)
print(arr)