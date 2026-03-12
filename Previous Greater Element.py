class Solution:
	def preGreaterEle(self, arr):
        n = len(arr)
        stack = []
        res = []
        for i in range(n):
            
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            res.append(-1 if not stack else arr[stack[-1]])
            
            stack.append(i)
        return res
