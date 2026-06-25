class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        parent = list(range(n*m))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rooty]= rootx
            
        d = {
            1 : {'L', 'R'},
            2 : {'U', 'D'},
            3 : {'L', 'D'},
            4 : {'D', 'R'},
            5 : {'L', 'U'},
            6 : {'U', 'R'},
        }

        def get_id(r, c):
            return r * m + c
        
        for r in range(n):
            for c in range(m):
                curr_type = grid[r][c]

                if c+1 < m:
                    right_type = grid[r][c+1]
                    if 'R' in d[curr_type] and 'L' in d[right_type]:
                        union(get_id(r,c), get_id(r, c+1))
                
                if r+1 < n:
                    down_type = grid[r+1][c]
                    if 'D' in d[curr_type] and 'U' in d[down_type]:
                        union(get_id(r,c), get_id(r+1, c))
                
        return find(get_id(0,0)) == find(get_id(n-1, m-1))