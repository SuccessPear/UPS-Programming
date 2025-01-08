from bisect import bisect
def sortedSum(a):
    # Write your code here
    sorted_list = [a[0]]
    f = a[0]
    result = f
    for i in range(1, len(a)):
        idx = bisect(sorted_list, a[i])
        tmp = 0
        for j in range(idx, len(sorted_list)):
            tmp += sorted_list[j]
        f += a[i]*(idx+1) + tmp
        result = (result + f) % (10**9 + 7)
        sorted_list.insert(idx, a[i])
    
    return result

a = [3, 9, 5, 8]
print(sortedSum(a))