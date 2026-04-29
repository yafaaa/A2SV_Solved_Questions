class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ans = [set() for _ in range(n)]
        incoming = [0] * n

        for parent, child in edges:
            graph[parent].append(child)
            incoming[child] += 1
        
        dq = deque([c for c in range(n) if not incoming[c]])

        while dq:
            node = dq.popleft()
            
            for child in graph[node]:
                ans[child].add(node)
                ans[child].update(ans[node])

                incoming[child] -= 1

                if not incoming[child]:
                    dq.append(child)
        return [sorted(list(s)) for s in ans]
        
            


        


