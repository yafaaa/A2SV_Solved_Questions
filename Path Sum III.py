# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def fun(root, curr=0):
            if not root:
                return
            curr += root.val
            if curr == targetSum:
                self.ans += 1
            fun(root.left, curr)
            fun(root.right, curr)

        def fun2(root):
            if not root:
                return
            fun(root)
            fun2(root.left)
            fun2(root.right)
        fun2(root)
        return self.ans
        
        
