from queue import Queue

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
    
    def preOrder(self):
        print(self.value)

        if self.left_child:
            self.left_child.preOrder()
        
        if self.right_child:
            self.right_child.preOrder()
    
    def inOrder(self):
        if self.left_child:
            self.left_child.inOrder()
        print(self.value)
        if self.right_child:
            self.right_child.inOrder()

    def postOrder(self):
        if self.left_child:
            self.left_child.postOrder()
        if self.right_child:
            self.right_child.postOrder()
        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            currentNode = queue.get()
            print(currentNode.value)

            if currentNode.left_child:
                queue.put(currentNode.left_child)
            
            if currentNode.right_child:
                queue.put(currentNode.right_child)

class BinarySearchTree:
    def __init__ (self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
    
    def insertNode(self, value) -> None:
        if value <= self.value and self.leftChild:
            self.leftChild.insertNode(value)
        elif value <= self.value:
            self.leftChild = BinarySearchTree(value)
        elif value > self.value and self.rightChild:
            self.rightChild.insertNode(value)
        else:
            self.rightChild = BinarySearchTree(value)
    
    def preOrder(self):
        print(self.value)

        if self.leftChild:
            self.leftChild.preOrder()
        
        if self.rightChild:
            self.rightChild.preOrder()
    
    def findNode(self, value) -> bool:
        if value < self.value and self.leftChild:
            return self.leftChild.findNode(value)
        if value > self.value and self.rightChild:
            return self.rightChild.findNode(value)
        
        return value == self.value

    def clearNode(self):
        self.value = None
        self.leftChild = None
        self.rightChild = None

    def findMinimumValue(self):
        if self.leftChild:
            return self.leftChild.findMinimumValue()
        else:
            return self.value
    
    def removeNode(self, value, parent) -> bool:
        if value < self.value and self.leftChild:
            return self.leftChild.removeNode(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.rightChild:
            return self.rightChild.removeNode(value, self)
        elif value > self.value:
            return False
        else:
            if self.leftChild is None and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = None
                self.clearNode()
            elif self.leftChild is None and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = None
                self.clearNode()
            elif self.leftChild and self.rightChild is None and self == parent.leftChild:
                parent.leftChild = self.leftChild
                self.clearNode()
            elif self.leftChild and self.rightChild is None and self == parent.rightChild:
                parent.rightChild = self.leftChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.leftChild:
                parent.leftChild = self.rightChild
                self.clearNode()
            elif self.rightChild and self.leftChild is None and self == parent.rightChild:
                parent.rightChild = self.rightChild
                self.clearNode()
            else:
                self.value = self.rightChild.find_minimum_value()
                self.rightChild.removeNode(self.value, self)
            
        return True
            

tree = BinaryTree('1')
tree.insert_left('2')
tree.insert_right('5')

bNode = tree.left_child
bNode.insert_right('4')
bNode.insert_left('3')

cNode = tree.right_child
cNode.insert_left('6')
cNode.insert_right('7')

bst = BinarySearchTree(15)
bst.insertNode(10)
bst.insertNode(8)
bst.insertNode(12)
bst.insertNode(20)
bst.insertNode(17)
bst.insertNode(25)
bst.insertNode(19)

#tree.bfs()
print(bst.removeNode(8, None))
print(bst.removeNode(17,None))
bst.preOrder()


