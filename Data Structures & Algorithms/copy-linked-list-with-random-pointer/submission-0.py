"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = Node(0)
        dc = dummy 
        curr = head 
        lookup = {}          # original node → its copy
        
        while curr:
            new_curr = Node(curr.val)
            dc.next = new_curr
            lookup[curr] = new_curr      # ← remember the pairing
            # moving pointers
            dc = dc.next
            curr = curr.next

        curr = head 
        copy_of_curr = dummy.next 

        while curr: 
            lookup[curr].random = lookup.get(curr.random)
            # moving pointer
            curr = curr.next 

        return dummy.next
        