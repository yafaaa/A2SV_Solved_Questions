class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        def dfs(source, visited):
            if source == destination:
                return True
            
            for nebr in d[source]:
                if nebr not in visited:
                    visited.add(nebr)
                    if dfs(nebr, visited):
                        return True
        return True if dfs(source, set()) else False