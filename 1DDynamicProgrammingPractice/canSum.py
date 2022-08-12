"""
# Recursive brute force initial solution

def canSum(target: int, nums: list[int]) -> bool:
    if target == 0: return True
    if target < 0: return False

    for num in nums:
        remainder = target - num
        if canSum(remainder, nums):
            return True

    return False
"""

def canSum(targetSum: int, numbers: list[int], memo={}) -> bool:
    if targetSum in memo: 
        return memo[targetSum]
    if targetSum == 0: 
        return True
    if targetSum < 0: 
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return False

#print(canSum(7, [2,3])) # true
#print(canSum(7, [5,3,4,7])) # true
print(canSum(7, [2,4])) # false
print(canSum(8, [2,3,5])) # true
#print(canSum(300, [7, 14])) # false