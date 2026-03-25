# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def fun(root, curr, s):
            if not root:
                return
            curr.append(root.val)
            s += root.val
            if not root.left and not root.right and s == targetSum:
                res.append(list(curr))  
            fun(root.left, curr, s)
            fun(root.right, curr, s)
            curr.pop()
        fun(root, [], 0)
        return res

            
