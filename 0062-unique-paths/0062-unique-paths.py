class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = dict()
        def fun(r, c):
            if r >m or c> n: # if out of bound
                return 0
            if r==m-1 and c==n-1: # if goal reached
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = fun(r+1, c) + fun(r, c+1)
            return memo[(r,c)]
            
        return fun(0,0)