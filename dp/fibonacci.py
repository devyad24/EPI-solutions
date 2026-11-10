cache = {}
def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-2) + fib(n-1)

    return cache[n]

print(f'{fib(0)}')


