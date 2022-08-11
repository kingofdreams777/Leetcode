"""
What could I do here? Arrays/hashing. I need to pop a value from the array and then multiply the rest of the values in the array together.
I could do some array splitting here, where I make a copy of the array with each index popped out. But how would I do that?
Could a hashmap/dictionary help here? What would I use the dictionary for?
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res

ex1 = [1,2,3,4]
ex2 = [-1,1,0,-3,3]
s = Solution()
print(s.productExceptSelf(ex1))
print(s.productExceptSelf(ex2))

