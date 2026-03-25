# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curr = 0
        def fun(root, curr, targetSum):
            if not root:
                return False
            curr += root.val
            if not root.left and not root.right:
                if curr == targetSum:
                    return True
                else:
                    return False
            
            return fun(root.left,curr, targetSum) or fun(root.right, curr, targetSum)
        
        return fun(root, 0, targetSum)
