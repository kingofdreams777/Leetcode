from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""
Hash map could help here. Neetcode said that Hashmaps typically can help in graph problems
Hashmap and recursion
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
