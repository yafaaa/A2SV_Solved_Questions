class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        y, x = len(grid), len(grid[0])

        cnt = 0
        for r in range(y):
            for c in range(x-1, -1,-1):
                if grid[r][c] >= 0:
                    break
                cnt += 1
        return cnt
