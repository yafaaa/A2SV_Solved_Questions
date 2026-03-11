# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        
        while curr:
            t = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = t
        return dummy.next
