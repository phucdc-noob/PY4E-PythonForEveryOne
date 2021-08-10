# using "Sieve of Eratosthenes" algorithm to count the primes numbers (prime numbers <= N) don't try n >= 100000000, it's too slow :(
def prime(n):
    if n <= 1:
        return
    result = []
    check = [True] * (n + 1)
    for i in range(2, n + 1):
        if check[i] == True:
            result.append(i)
            for j in range(2 * i, n + 1, i):
                check[j] = False
    return result

print(*prime(100000000), sep = " ")