
# Recursive solution for this problem that is fairly slow
# Brute force solution is typically the logical first step.
# look for brute force solution first and foremost
def gridTraveler(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

# memoization! If we have good recursion in the brute force solution
# memoization is very formulaic
# big O complexity is now O(m + n)?
# space complexity is O(m + n)
def gridTravelerD(m, n, memo={}):
    key = (m, n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[key] = gridTravelerD(m - 1, n, memo) + gridTravelerD(m, n - 1, memo)
    return memo[key]


print(gridTravelerD(1, 1))
print(gridTravelerD(2, 3))
print(gridTravelerD(3, 2))
print(gridTravelerD(3, 3))
print(gridTravelerD(18, 18))