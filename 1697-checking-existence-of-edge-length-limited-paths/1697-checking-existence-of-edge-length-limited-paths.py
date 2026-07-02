class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        
        sorted_queries = []
        for i, (u, v, limit) in enumerate(queries):
            sorted_queries.append((limit, u, v, i))
        
        sorted_queries.sort(key=lambda x: x[0])
        
        edgeList.sort(key=lambda x: x[2])
        
        dsu = DSU(n)
        ans = [False] * len(queries)
        
        edge_idx = 0
        num_edges = len(edgeList)
        
        for limit, u, v, original_idx in sorted_queries:

            while edge_idx < num_edges and edgeList[edge_idx][2] < limit:
                node1, node2, weight = edgeList[edge_idx]
                dsu.union(node1, node2)
                edge_idx += 1
            
            if dsu.find(u) == dsu.find(v):
                ans[original_idx] = True
                
        return ans