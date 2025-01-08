def straight_insertion_sort(arr: list[float]):
    for i in range(len(arr)):
        tmp = arr[i]
        idx = i - 1
        
        while(idx >= 0 and tmp < arr[idx]):
            arr[idx+1] = arr[idx]
            idx -= 1
        
        arr[idx+1] = tmp
        

arr = [3,1,2,5,4]
straight_insertion_sort(arr)
print(arr)