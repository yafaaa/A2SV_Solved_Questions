class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def inbound(nw_r, nw_c):
            return 0 <= nw_r < len(grid) and 0 <= nw_c < len(grid[0])
        
        dq = deque([(r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 2])
        cnt = 0
        while dq:
            lgth = len(dq)
            f = False
            for _ in range(lgth):
                r, c = dq.popleft()
                for dr, dc in direction:
                    nw_r = r + dr
                    nw_c = c + dc
                    if inbound(nw_r, nw_c) and grid[nw_r][nw_c]==1:
                        f = True
                        dq.append((nw_r, nw_c))
                        grid[nw_r][nw_c] = 2
            cnt += 1 if f else 0
        return -1 if any(row.count(1) for row in grid) else cnt
        
