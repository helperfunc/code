"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # prev.val <= insertVal <= cur.val
        # (prev.val > cur.val) and (insertVal >= prev.val or insertVal <= cur.val)
        # prev == head
        # prev.next = Node(insertVal, cur)
        if head == None:
            n = Node(insertVal)
            n.next = n
            return n
        
        prev, cur = head, head.next
        while True:
            is_inserted = False
            if prev.val <= insertVal and insertVal <= cur.val:
                is_inserted = True
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    is_inserted = True
            if is_inserted:
                prev.next = Node(insertVal, cur)
                return head
            prev = cur
            cur = cur.next
            if prev == head:
                prev.next = Node(insertVal, cur)
                break
        
        return head
