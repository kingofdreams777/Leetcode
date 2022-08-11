from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        base case is root is null, I return 0.
        A depth first search would work well here. That way I can traverse through the tree to the deepest part first and keep track of all the nodes I visit with a
        variable.
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



ex1 = TreeNode(3)
ex1.left = TreeNode(9)
ex1.right = TreeNode(20)
n1 = ex1.right
n1.left = TreeNode(15)
n1.right = TreeNode(7)

s = Solution()
print(s.maxDepth(ex1))


    
