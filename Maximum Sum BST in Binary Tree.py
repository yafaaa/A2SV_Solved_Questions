# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def fun(root):
            nonlocal ans
            if not root:
                return True, float('-inf'), float('inf'), 0
            
            l_bst, left_max, left_min, lcurr_sum = fun(root.left)
            r_bst, right_max, right_min, rcurr_sum = fun(root.right)

            c_bst = False

            if l_bst and r_bst:
                if left_max < root.val and root.val < right_min:
                    c_bst = True
                    ans = max(ans, root.val+lcurr_sum+rcurr_sum)
            
                return c_bst, max(left_max,right_max, root.val), min(right_min, left_min, root.val), root.val+lcurr_sum+rcurr_sum
            return False, float('-inf'), float('inf'), 0

        fun(root)
        
        return ans
