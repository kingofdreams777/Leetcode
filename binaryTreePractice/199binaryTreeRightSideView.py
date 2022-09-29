import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                if rightSide:
                    res.append(rightSide.val)

        return res

ex1 = TreeNode(1)
ex1.left = TreeNode(2)
ex1.right = TreeNode(3)
n1 = ex1.right
n1.right = TreeNode(4)

ex2 = TreeNode(1)
ex2.right = TreeNode(3)

ex3 = TreeNode(1)
ex3.left = TreeNode(2)

s = Solution()
print(s.rightSideView(ex1))
print(s.rightSideView(ex2))
print(s.rightSideView(ex3))
