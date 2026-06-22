# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node, f):
            if not node:
                return 0
            skip = dp(node.right, 0) + dp(node.left, 0)
            take = 0
            if f != 1:
                take = node.val + dp(node.right, 1) + dp(node.left, 1)
            return max(skip, take)
        return dp(root, 0)
            
