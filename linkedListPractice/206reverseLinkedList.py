from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#two pointer solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        prev = None

        while cur:
            switch = cur.next
            cur.next = prev
            prev = cur
            cur = switch
        
        return prev

                

ex1 = ListNode(1)
ex1.next = ListNode(2)
n2 = ex1.next
n2.next = ListNode(3)
n3 = n2.next
n3.next = ListNode(4)
n4 = n3.next
n4.next = ListNode(5)

s = Solution()
print(s.reverseList(ex1))