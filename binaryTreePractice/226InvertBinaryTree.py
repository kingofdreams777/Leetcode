from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    First thing I need to do is examine base case. IF root is None, return None.
    After that, it's a matter of 
    """
    if not root:
        return None

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        currentNode = queue.get()

        if currentNode.left:
            queue.put(currentNode.left)
        if currentNode.right:
            queue.put(currentNode.right)
        
        switch = currentNode.left
        currentNode.left = currentNode.right
        currentNode.right = switch
    

ex1 = TreeNode(4)
ex1.left = TreeNode(2)
ex1.right = TreeNode(7)
node2 = ex1.left
node2.left = TreeNode(1)
node2.right = TreeNode(3)
node3 = ex1.right
node3.right = TreeNode(9)
node3.left = TreeNode(6)