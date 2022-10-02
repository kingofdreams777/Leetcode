# Recursive version of Fibinocci sequence. Very slow when trying to call numbers bigger than 20 or so
def fib(n):
    if (n <= 2):
        return 1
    res = fib(n -1) + fib(n - 2)
    return res

# Dynamic programming version of fibinocci
# memoization: strategy to solve dynamic programming problems
# store duplicate sub problems to get the results later on
# fast access data structure
# python dictionary? Keys are the argument to the function, value will be the return value
def fibD(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibD(n - 1, memo) + fibD(n - 2, memo)
    return memo[n]

print(fibD(0))
