array = [1, 2, 5, 7, 8, 9]


def binary_search(x, arr):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = int((right+left)/2)
        if x > arr[mid]:
            left = mid + 1
        elif x < arr[mid]:
            right = mid - 1
        else:
            return mid, left
    return -1

print(binary_search(5, array))