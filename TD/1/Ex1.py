# Remove duplicates from an array
# Conditions:
# - array is sorted in non decreasing order
# - Remove the duplicate in place
# - The relative order of the element should be same
# ==> return the number of unique elements
arr = [1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 7, 8, 8, 9, 10, 10]
print(id(arr))
def remove_duplicate(arr):
    if not arr:
        return 0
    current = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[current]:
            arr[current+1] = arr[i]
            current += 1
    
    return current + 1

print(remove_duplicate(arr))

print(id(arr))
print(arr)

