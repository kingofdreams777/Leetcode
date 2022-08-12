"""
need to learn python bit shifting. It looks at every bit. even the numbers that aren't 1's
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2
            n = n >> 1
        return res
    
    def hammingWeightBetter(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
