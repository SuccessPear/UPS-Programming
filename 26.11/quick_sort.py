def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr: list, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, high)

arr = [1, 4, 9, 6, 5, 3, 7]
quick_sort(arr, 0, len(arr)-1)
print(arr)