from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            qLen = len(queue)
            subList = []
            for i in range(qLen):
                node = queue.pop(0)
                if node:
                    subList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if subList:
                res.append(subList)


        return res

ex1 = TreeNode(3)
ex1.left = TreeNode(9)
n1 = ex1.left
ex1.right = TreeNode(20)
n2 = ex1.right
n2.left = TreeNode(15)
n2.right = TreeNode(7)

s = Solution()
print(s.levelOrder(ex1))


        