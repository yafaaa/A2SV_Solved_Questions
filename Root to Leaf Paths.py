from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root):
        result = []
        def fun(root, string):
            if not root:
                return
            string += str(root.data)
            if not root.left and not root.right:
                result.append([int(ch) for ch in string])
            else:
                fun(root.left, string)
                fun(root.right, string)
        fun(root, "")
        return result
        
