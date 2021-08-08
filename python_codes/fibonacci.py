# count the nth fibonacci number with dynamic programming (Quy hoach dong)  
# Fibonacci: 1 1 2 3 5 8 13 ...

def fibonacci(n):
    result = [0] * (n + 1)
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]

print(fibonacci(3))