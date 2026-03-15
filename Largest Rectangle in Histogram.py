class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        next_mn = [n-i for i in range(n)] 
        prev_mn = [i for i in range(n)]
        mx = float('-inf')
        
        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                p = stack.pop()                    
                next_mn[p] = i-p 
            
            stack.append(i)
        stack = []

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                p = stack.pop()                    
                next_mn[p] = i-p 
            if stack:
                prev_mn[i] = i - stack[-1] - 1

            stack.append(i)

        for i in range(n):
            mx = max(mx, heights[i] * (next_mn[i]+prev_mn[i]))
        
        return mx
        

