class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m = len(grid), len(grid[0])
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        cnt = 0

        def inbound(r, c):
            return 0<= r <n and 0<= c <m

        def dfs(r,c):

            for dr, dc in direction:
                nw_r = r + dr
                nw_c = c + dc
                if inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited and grid[nw_r][nw_c] == "1":
                    visited.add((nw_r, nw_c))
                    dfs(nw_r, nw_c)

        

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r,c)
                    cnt += 1
                    
        return cnt
                    
