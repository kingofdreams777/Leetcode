class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums [i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)



ex1 = [10,9,2,5,3,7,101,18]
ex2 = [0,1,0,3,2,3]