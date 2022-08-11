def fib(n):
    if (n <= 2):
        return 1
    res = fib(n -1) + fib(n - 2)
    return res

print(fib(50))
