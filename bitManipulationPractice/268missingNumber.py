class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res

ex1 = [3,0,1]
ex2 = [9,6,4,2,3,5,7,0,1]

s = Solution()
print(s.missingNumber(nums=ex1))
print(s.missingNumber(nums=ex2))

print(3 ^ 5)