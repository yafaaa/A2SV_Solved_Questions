"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
            dq = deque()
            if root:
                dq = deque([root])
            ans = 0
            while dq:
                l = len(dq)
                ans += 1
                for i in range(l):
                    f = dq.popleft()
                    if f.children:
                        dq.extend(f.children)
            return ans
