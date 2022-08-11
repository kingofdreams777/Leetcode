from queue import Queue
from typing import Optional
from xmlrpc.client import boolean


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def insertNode(self, data) -> None:
        if data <= self.data and self.left:
            self.left.insertNode(data)
        elif data <= self.data:
            self.left = Node(data)
        elif data > self.data and self.right:
            self.right.insertNode(data)
        else:
            self.right = Node(data)
    

ex1 = Node(4)
ex1.insertNode(2)
bNode = ex1.left
bNode.insertNode(1)
bNode.insertNode(3)
ex1.insertNode(6)
cNode = ex1.right
cNode.insertNode(1)
cNode.insertNode(7)

def check(root, minValue, maxValue):

    if root is None:
        return True
    
    if root.data < minValue or root.data > maxValue:
        return False
    
    return check(root.left, minValue, root.data) and check(root.right, root.data, maxValue)


def checkBST(root: Optional[Node]):
    """
    BFS is not a recursive search! I don't have to call the BFS function everytime I step down through the tree. The queue handles are the recursion, therefore I can
    hold onto the root value the whole time!
    """
    if not root:
        return True
    values = {}
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        currentNode = queue.get()
        if currentNode.data in values:
            values[currentNode.data] += 1
        else:
            values[currentNode.data] = 1
        if currentNode.left:
            queue.put(currentNode.left)
        if currentNode.right:
            queue.put(currentNode.right)
    
    for key in values:
        if values[key] > 1:
            return False
    
    return check(root,0,10000)


print(checkBST(ex1))
    
