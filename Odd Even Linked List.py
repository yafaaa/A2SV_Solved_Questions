# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        cnt = 0
        curr1 = dummy1
        curr2 = dummy2
        curr = head

        while curr:
            t = curr.next
            if not cnt%2:
                curr1.next = curr
                curr.next = None
                curr1 = curr1.next
    
            else:
                curr2.next = curr
                curr.next = None
                curr2 = curr2.next
            curr = t
            cnt += 1
        curr1.next = dummy2.next
        return dummy1.next
        
