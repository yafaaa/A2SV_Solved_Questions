class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in [(0, 1), (1, 0)]:
                        nr, nc = r + dr, c + dc
                        if nr < n and nc < n and grid[nr][nc] == 1:
                            dsu.union(r * n + c, nr * n + nc)
        
        res = max(dsu.size) if 1 in [cell for row in grid for cell in row] else 0
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_roots = set()
                    current_size = 1
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = dsu.find(nr * n + nc)
                            if root not in seen_roots:
                                current_size += dsu.size[root]
                                seen_roots.add(root)
                    res = max(res, current_size)
                    
        return res