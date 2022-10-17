from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

        return None

ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(7)
n1 = ex1.left
n1.left = TreeNode(1)
n1.right = TreeNode(3)

s = Solution()
print(s.searchBST(ex1, 2).val)