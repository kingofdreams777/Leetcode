class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums + nums
        return ans

s = Solution()

ex1 = [1,2,1]
ex2 = [1,3,2,1]

print(s.getConcatenation(ex1))
print(s.getConcatenation(ex2))