class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        direction = [(1,0), (-1,0), (0,1), (0, -1)]

        def inbound(nw_r, nw_c):
            return 0<= nw_r < n and 0<= nw_c <m
        cnt = 0
        visited = set()

        def dfs(r, c,visited):
            nonlocal cnt
    
            for dr, dc in direction:
                nw_r = r+dr
                nw_c = c+dc
                if inbound(nw_r, nw_c) and grid[nw_r][nw_c] == 1 and (nw_r, nw_c) not in visited:
                    visited.add((nw_r, nw_c))
                    dfs(nw_r, nw_c, visited)
                elif (nw_r, nw_c) not in visited:
                    cnt += 1


        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    visited.add((r,c))
                    dfs(r, c, visited)
                    return cnt

        
        
