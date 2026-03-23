# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = dict()

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.d[inorder[i]] = i
        return self.fun(preorder, 0, len(inorder) - 1)
        
    def fun(self, preorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end or not preorder:
            return None
        
        val = preorder[0]
        node = TreeNode(val)
        
        idx = self.d[val]
        
        preorder.pop(0)
        
        
        node.left = self.fun(preorder, start, idx - 1)
        
        node.right = self.fun(preorder, idx + 1, end)
        
        return node
