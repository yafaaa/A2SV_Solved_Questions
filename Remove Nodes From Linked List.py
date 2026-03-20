# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            prev = None
            curr = head
            while curr:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t
            return prev
        head = rev(head)
        dummy = ListNode(0)
        curr_d = dummy
        curr = head
        while curr:
            t = curr.next
            if curr.val >= curr_d.val:
                curr_d.next = curr
                curr.next = None
                curr_d = curr_d.next
            curr = t
        return rev(dummy.next)
