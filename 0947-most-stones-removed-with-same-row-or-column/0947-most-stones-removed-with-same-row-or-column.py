class Solution:

    def removeStones(self, stones: list[list[int]]) -> int:
        parent = {}

        def find(i):
            
            if i not in parent:
                parent[i] = i
      
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for r, c in stones:
            union(r, ~c)
        
        comp = len({x for x in parent if x == parent[x]})

        return len(stones) - comp