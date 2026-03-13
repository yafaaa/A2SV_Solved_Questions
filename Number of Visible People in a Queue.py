class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        res = [0] * n

        for i in range(n):

            while stack and heights[stack[-1]] < heights[i]:
                res[stack.pop()] += 1
            
            if stack:
                res[stack[-1]] += 1
            
            stack.append(i)
        return res
 #=================intutitive form=============
        # n = len(heights)
        # stack = []
        # next_g = [0] * n
        # prev_g = [0] * n

        # for i in range(n):

        #     while stack and heights[stack[-1]] < heights[i]:
        #         next_g[stack.pop()] += 1
            
        #     stack.append(i)
        # stack = []
        # for i in range(n):

        #     while stack and heights[stack[-1]] < heights[i]:
        #         stack.pop()

        #     if stack:
        #         prev_g[stack[-1]] += 1

        #     stack.append(i)
        
        # for i in range(n):
        #     next_g[i] += prev_g[i]
        # return next_g
