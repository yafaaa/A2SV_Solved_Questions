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
        return self.fun(preorder, inorder)
        
        
    def fun(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        node = TreeNode(preorder[0])
        idx = self.d[preorder[0]]
        preorder.pop(0)
        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])
        return node
        
