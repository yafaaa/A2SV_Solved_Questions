class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        memo = {}
        def dp(r, c):
            if r == n or c == m:
                return float('inf')
            if r == n-1 and c == m-1:
                return grid[n-1][m-1]

            if (r,c) in memo:
                return  memo[(r,c)]
            
            down = grid[r][c] + dp(r+1, c)

            left = grid[r][c] + dp(r, c+1)

            memo[(r,c)] = min(left, down)
            return memo[(r,c)]
        return dp(0, 0)
