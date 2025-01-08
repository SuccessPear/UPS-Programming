def fibonacci(n, history_map):
    if n in history_map:
        return history_map[n]
    if n == 1:
        history_map[1] = 1
        return 1
    elif n == 0:
        history_map[0] = 0
        return 0
    result = fibonacci(n-1, history_map) + fibonacci(n-2, history_map)
    history_map[n] = result
    return result

history_map = {}
#print(fibonacci(5, history_map))

def fibo2(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo2(n-1) + fibo2(n-2)

#print(fibo2(5))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def hamonic_sum(n):
    if n == 1:
        return 1
    return 1.0/n + hamonic_sum(n-1)

#print(hamonic_sum(2))

# b is positive integer
def pow1(a, b):
    if a == 0 or a == 1:
        return a
    
    if b == 1:
        return a
    return a * pow1(a, b-1)

print(pow1(2, 3))
