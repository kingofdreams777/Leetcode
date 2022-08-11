from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        if not head:
            return False
        while head:
            if head in visited:
                return True
            elif not head:
                return False
            else:
                visited[head] = 0
                head = head.next