def twoSum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        if (numbers[l] + numbers[r]) == target:
            return [l+1,r+1]
        if (numbers[l] + numbers[r]) > target:
            r -= 1
        if (numbers[l] + numbers[r]) < target:
            l += 1

ex1 = [2,7,11,15]
t1 = 9

print(twoSum(ex1, t1))