"""
    m = target sum
    n = len(numbers)

    Brute Force
    time: O(n^m * m)
    space: O(m^2)
"""
def bestSum(targetSum: int, numbers: list[int]) -> list[int]:
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            combination = [*remainderCombination, num]

            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    return shortestCombination

"""
memoized complexity
time: O(m^2 * n)
space: O(m^2)
"""

def bestSumD(targetSum: int, numbers: list[int], memo={}) -> list[int]:
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSumD(remainder, numbers, memo)
        if remainderCombination != None:
            combination = [*remainderCombination, num]

            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination

print(bestSumD(7, [5,3,4,7],{}))
print(bestSumD(8, [2,3,5],{}))
print(bestSumD(8, [1,4,5],{}))
print(bestSumD(100, [1,2,5,25],{}))