class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        ex_n = n * 3
        e_grid = [[0] * ex_n for _ in range(ex_n)]

        for r in range(n):
            for c in range(n):
                br, bc = r*3, c*3
                if grid[r][c] == '/':
                    e_grid[br][bc+2] = 1
                    e_grid[br+1][bc+1] = 1
                    e_grid[br+2][bc] = 1
                elif grid[r][c] == '\\':
                    e_grid[br][bc] = 1
                    e_grid[br+1][bc+1] = 1
                    e_grid[br+2][bc+2] = 1
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rooty] = rootx
        

        for r in range(ex_n):
            for c in range(ex_n):
                if e_grid[r][c] == 0:

                    if r+1 < ex_n and e_grid[r+1][c] != 1:
                        union((r, c), (r+1, c))
                    
                    if c+1 < ex_n and e_grid[r][c+1] != 1:
                        union((r, c), (r, c+1))

        return len([x for x in parent if find(x) == x])
        

        

        


