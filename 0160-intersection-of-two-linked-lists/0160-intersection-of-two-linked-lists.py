# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        curr = headA

        while curr:
            seen.add(curr)
            curr = curr.next
        
        currb = headB

        while currb:
            if currb in seen:
                return currb
            currb = currb.next
        
        return None