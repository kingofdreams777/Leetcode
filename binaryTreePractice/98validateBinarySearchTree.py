from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root: Optional[TreeNode], minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val > maxVal:
                return False
            return check(root.left, minVal, root.data) and check(root.right, root.data, maxVal)
        
        return check(root, -2147483648, 2147483647)


        