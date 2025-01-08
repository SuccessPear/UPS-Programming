# If we use the most straight forward algorithm, which is check the largest value in the k-length window
# The complexity of this algorithm is n*k
# An upgrade way is to use the k-length sorted list, and update it using binary search algorithm
# It's still O(n*k) because of the insertion which takes O(k) but it will be faster to get the largest number in the window
# Python have a library that support this, which is bisect or I can implement it myself
import bisect

def find_max_of_sliding_window(nums: list[int], k):
    result = []
    sorted_list = []
    # initialize the k-length sorted_list with k first elements
    for i in range(k):
        bisect.insort(sorted_list, nums[i])
    
    result.append(sorted_list[-1])
    for i in range(k, len(nums)):
        # remove the i-k th element from the list
        idx = bisect.bisect_left(sorted_list, nums[i-k])
        sorted_list.pop(idx)
        # add the ith element to the list
        bisect.insort(sorted_list, nums[i])
        # add the last value of sorted_list to the result list
        result.append(sorted_list[-1])
    
    return result

#T = [1,3,-1,-3,5,3,6,7]
#k = 3

T = [1, -1]
k = 1

print(find_max_of_sliding_window(T, k))