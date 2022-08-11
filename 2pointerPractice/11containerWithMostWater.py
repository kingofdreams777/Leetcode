class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxWater = max(area, maxWater)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxWater

ex1 = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(ex1))