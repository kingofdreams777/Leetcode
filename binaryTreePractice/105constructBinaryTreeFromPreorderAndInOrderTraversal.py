from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

"""
Notes on this problem:
    The preorder list gives us the nodes starting with root, down the left side, then down the right side. The in order solution
    gives us nodes down the left side, then root, then down the right side. The two lists can be combined where the root is the midpoint
    of the array in order. So we cut the array at the midpoint of root, and then call the function recursively on itself to build the rest
    of the tree out. May need to watch this video again to really understand it.
"""
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root