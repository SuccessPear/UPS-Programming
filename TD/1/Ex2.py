nums1 = [4, 9, 5, 23, 4,2,5,6,1,5,3,5,6,7]
nums2 = [9, 4, 9, 8, 4, 3,4,1,3,6,4,2,1,1,1,1]

nums1.sort()
nums2.sort()

def remove_duplicate(arr):
    current = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[current]:
            arr[current+1] = arr[i]
            current += 1
    
    return current + 1

k1 = remove_duplicate(nums1)
k2 = remove_duplicate(nums2)
print(nums1)
print(nums2)

def find_element_in_sorted_array(x, arr):
    left = 0
    right = len(arr) - 1
    while (left <= right):
        mid = int((right+left)/2)
        if x > arr[mid]:
            left = mid + 1
        elif x < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1

result = []
tmp = 0
for i in range(k1):
    idx = find_element_in_sorted_array(nums1[i], nums2[tmp:k1])
    if idx != -1:
        result.append(nums1[i])
        tmp = idx
print(result)
    