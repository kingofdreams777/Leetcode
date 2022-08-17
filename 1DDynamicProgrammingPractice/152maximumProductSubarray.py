"""
Simple brute force solution.
Works when all integers are positive
"""
"""
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        product = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                subarray = nums[i:j]
                potential = 1
                for k in subarray:
                    potential *= k
                product = max(product, potential)

        
        return product
"""
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums) # 0 -> [-1]
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1,1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMin)

        return res



ex1 = [2,3,-2,4]
ex2 = [-2,0,-1]
s = Solution()
print(s.maxProduct(ex1))
print(s.maxProduct(ex2))
