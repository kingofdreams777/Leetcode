import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

"""
My Old Solution below. Didn't work on some test cases
Used recursion and Depth first search to navigate through paths. Worked on the two listed test cases
"""
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        maxSumLeft, maxSumRight = 0, 0

        if not root.left and not root.right:
            return root.val
        
        if root.left:
            maxSumLeft = self.maxPathSum(root.left)
        if root.right:
            maxSumRight += self.maxPathSum(root.right)

        res = max(maxSum + maxSumLeft + maxSumRight, maxSumLeft, maxSumRight)

        return res
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # means we can modify in recursive function easier

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)

            #compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(3)

ex2 = TreeNode(-10)
ex2.left = TreeNode(9)
ex2.right = TreeNode(20)
right = ex2.right
right.left = TreeNode(15)
right.right = TreeNode(7)

ex3 = TreeNode(-3)
ex4 = TreeNode(2)
ex4.left = TreeNode(-1)

s = Solution()
print(s.maxPathSum(ex1))
print(s.maxPathSum(ex2))
print(s.maxPathSum(ex3))
