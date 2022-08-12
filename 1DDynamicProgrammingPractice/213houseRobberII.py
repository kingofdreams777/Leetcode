class Solution:
    def rob(self, nums: list[int]) -> int:
        l1 = self.helper(nums[1:])
        l2 = self.helper(nums[:-1])
        return max(nums[0], l1, l2)

    def helper(self, nums: list[int]):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        

        return rob2

ex1 = [2,3,2]
ex2 = [1,2,3,1]
ex3 = [1,2,3]

s = Solution()
print(s.rob(ex1))
print(s.rob(ex2))
print(s.rob(ex3))