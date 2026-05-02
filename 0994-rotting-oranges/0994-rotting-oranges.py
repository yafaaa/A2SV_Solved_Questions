class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def inbound(nw_r, nw_c):
            return 0 <= nw_r < len(grid) and 0 <= nw_c < len(grid[0])

        fresh_count = 0
        dq = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        time = 0
        while dq and fresh_count>0:
            time += 1
            lgth = len(dq)
            for _ in range(lgth):
                r, c = dq.popleft()
                for dr, dc in direction:
                    nw_r = r + dr
                    nw_c = c + dc
                    if inbound(nw_r, nw_c) and grid[nw_r][nw_c]==1:
                        fresh_count -= 1
                        dq.append((nw_r, nw_c))
                        grid[nw_r][nw_c] = 2

        return -1 if fresh_count else time
        
