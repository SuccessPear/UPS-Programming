def relative_sort(A, B):
    f = [0] * 1000
    for item in A:
        f[item] = f[item] + 1
    