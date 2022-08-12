"""
m = target sum
n = numbers.length

time: O(n^m * m)
space: O(m)
"""


def howSum(targetSum: int, numbers: list[int]) -> list[int]:
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)

        if remainderResult != None:
            return [*remainderResult, num]

    return None

"""
memoized version
time: O(n*m^2)
space: O(m)
"""

def howSumD(targetSum: int, numbers: list[int], memo = {}) -> list[int]:
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSumD(remainder, numbers, memo=memo)

        if remainderResult != None:
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None

print(howSumD(7, [2,3],memo={})) # [3, 2, 2]
print(howSumD(7, [5,3,4,7], memo={})) # [4, 3]
print(howSumD(7, [2,4], memo={})) # none
print(howSumD(8, [2,3,5], memo={})) # [2, 2, 2 ,2]
print(howSumD(300, [7, 14], memo={})) # none