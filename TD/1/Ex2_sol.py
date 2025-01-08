def intersection(nums1, nums2):
    p1 = 0
    p2 = 0
    N = len(nums1)
    M = len(nums2)
    
    nums1.sort()
    nums2.sort()
    
    I = set()
    
    while p1 < N and p2 < M:
        if nums1[p1] == nums2[p2]:
            I.add(nums1[p1])
        elif nums1[p1] < nums2[p2]:
            p1 = p1 + 1
        else:
            p2 = p2 + 1
    return list(I)

nums1 = [4, 9, 5, 23, 4,2,5,6,1,5,3,5,6,7]
nums2 = [9, 4, 9, 8, 4, 3,4,1,3,6,4,2,1,1,1,1]

print(intersection(nums1, nums2))