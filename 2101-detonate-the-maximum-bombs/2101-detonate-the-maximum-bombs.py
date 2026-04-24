class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                if (y2-y1) ** 2 + (x2-x1) ** 2 <= r1**2:
                    graph[i].append(j)
        mx = 1
        for i in range(n):
            dq = deque([i])
            visited = set([i])
            cnt = 0
            while dq:
                parent = dq.popleft()
                cnt += 1
                for child in graph[parent]:
                    if child not in visited:
                        dq.append(child)
                        visited.add(child)
            mx = max(mx, cnt)
        return mx

                

        
