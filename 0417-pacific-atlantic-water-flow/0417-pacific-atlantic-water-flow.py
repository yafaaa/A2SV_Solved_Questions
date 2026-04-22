class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(heights), len(heights[0])

        def dfs(r, c, visited):
                    
                    for dr, dc in direction:
                        nw_r = r + dr
                        nw_c = c + dc

                        if 0 <= nw_r < n and 0 <= nw_c < m:
                            if heights[r][c] >= heights[nw_r][nw_c] and (nw_r, nw_c) not in visited:
                                visited.add((nw_r, nw_c))
                                dfs(nw_r, nw_c, visited)
                                continue
                        if nw_c < 0 or nw_r < 0:
                            pa[0] = True
                             
                        if nw_c >= m or nw_r >= n:
                            pa[1] = True

        ans = []
        for r in range(n):
            for c in range(m):
                pa =  [False, False]
                dfs(r, c, {(r,c)})
                if pa[0] and pa[1]:
                    ans.append([r,c])
        return ans
