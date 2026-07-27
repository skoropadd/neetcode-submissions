# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the mid and cut into two pieces 
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        head2 = slow.next     # always — no branch
        slow.next = None      # always — no branch

        # 2. reverse the second part 
        curr = head2
        prev = None 
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        # new head = prev 

        # 3. blend a second list in place to the first one 
        curr_1 = head
        curr_2 = prev
        while curr_2: 
             temp_1 = curr_1.next
             temp_2 = curr_2.next 

             curr_1.next = curr_2
             curr_2.next = temp_1

             curr_1 = temp_1
             curr_2 = temp_2