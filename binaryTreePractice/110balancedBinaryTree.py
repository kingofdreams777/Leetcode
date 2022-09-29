from optparse import Option
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    My old solution. I was on the right path for sure
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        lheight, rheight = 0, 0
        def dfs(node):
            if node.left:
                lheight += dfs(node.left)[0]
            if node.right:
                rheight += dfs(node.right)[1]
            return [lheight, rheight]

        lheight, rheight = dfs(root)
        res = abs(lheight - rheight)

        return True if res <= 1 else False
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

ex1 = TreeNode(3)
ex1.left = TreeNode(9)
ex1.right = TreeNode(20)
r1 = ex1.right
r1.left = TreeNode(15)
r1.right = TreeNode(7)

ex2 = TreeNode(1)
ex2.left = TreeNode(2)
ex2.right = TreeNode(2)
l1 = ex2.left
l1.left = TreeNode(3)
l1.right = TreeNode(3)
l2 = l1.left
l2.left = TreeNode(4)
l2.right = TreeNode(4)

s = Solution()
print(s.isBalanced(ex1))
print(s.isBalanced(ex2))