#Idea: a is the number of 1 step taken
#      b is the number of 2 step taken
# First we find all combination of a and b such that a + 2*b = n
# Then we calculate the number of permutation for that by this formula: (a + b)!/a!/b!    (repeated permutation)

# This one is slow because it doesnt reuse the previous permitation
def repeated_permutation(a, b):
    result = 1
    for i in range(1, b+1):
        result = result * (a+i)/i
    return result

def climb_stair(n):
    total = 0
    
    tmp = 1
    total += tmp
    for b in range(1, int(n/2)+1):
        a = n - 2*b
        
        tmp = tmp * (a+1)*(a+2)/(a+b+1)/b
        total += tmp
    
    return int(total)

print(climb_stair(4))