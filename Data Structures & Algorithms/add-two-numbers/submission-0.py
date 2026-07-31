# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy
        carry_val = 0 

        while l1 and l2: 
            total = l1.val + l2.val + carry_val
            val = total % 10
            curr.next = ListNode(val)
            carry_val = total // 10

            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        
        left = l1 or l2

        while left:
            total = left.val + carry_val
            val = total % 10
            curr.next = ListNode(val)
            carry_val = total // 10

            left = left.next
            curr = curr.next

        if carry_val > 0: 
            curr.next = ListNode(carry_val)
        
        return dummy.next