def bubble_sort(arr: list):
    n = len(arr)
    
    for i in reversed(range(n)):
        for j in range(i):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5,3,8,2,1]
print(bubble_sort(arr))