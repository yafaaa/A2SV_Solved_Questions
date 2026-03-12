class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        stack = []
        res = [-1] * n
        for i in range(n):
            
            while stack and arr[stack[-1]] < arr[i]:
                res[stack.pop()] = arr[i]
                
            stack.append(i)
        return res
        
