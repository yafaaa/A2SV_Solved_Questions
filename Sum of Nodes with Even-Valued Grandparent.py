# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def fun(root, curr=0):
            if not root:
                return curr
            curr += root.left.val if root.left else 0
            curr += root.right.val if root.right else 0
            return curr

       
        def fun3(root):
            if not root:
                return
            if not root.val%2:
                self.ans += fun(root.left) + fun(root.right)
            fun3(root.left)
            fun3(root.right)
        fun3(root)
        return self.ans
        
        

            
