from typing import Optional


class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            else:
                return cur
        