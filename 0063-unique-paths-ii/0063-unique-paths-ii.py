class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(r, c):
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == n-1 and c == m-1:
                return 1
                
            right = down = 0
            if r+1 < n:
                down = dp(r+1, c)
            if c+1 < m:
                right = dp(r, c+1)
            return down + right
        return dp(0, 0)