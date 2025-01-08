# ideas: Calculate all posible distances, store them in sorted list (ascending order) which has at most k elements
# -If new distances is smaller than the last elements, insert it the list (follow the sorted order)
# and pop the last element (if length of the list is greater than k)
# -At the end, return the last element of the list

# Import this library to create a sorted list
import bisect

def calculate_distance(x, y):
    if (x > y):
        return x - y
    return y - x

def find_kth_smallest_distance(arr, k):
    sorted_list = []
    
    # 2 loop for calculating the distance and insert them in the sorted_list
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # always insert the first distance
            if len(sorted_list) == 0:
                sorted_list.append(calculate_distance(arr[i], arr[j]))
                continue
            
            # If the distance is smaller than the last element, insert it to the sorted_list
            if calculate_distance(arr[i], arr[j]) < sorted_list[-1]:
                bisect.insort(sorted_list, calculate_distance(arr[i], arr[j]))
                
                # If length of the sorted_list > k, pop the last element (we only care about the first k-th smallest distances)
                if len(sorted_list) > k:
                    sorted_list.pop()
    
    return sorted_list[-1]

arr = [10, 4, 2, 9, 1, 4, 6]
k = 6
print(find_kth_smallest_distance(arr, k))