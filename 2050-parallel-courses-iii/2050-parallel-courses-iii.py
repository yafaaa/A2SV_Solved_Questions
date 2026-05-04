class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        graph = [[] for _ in range(n+1)]
        incoming = [0] * (n+1)
        for parent, child in relations:
            graph[parent].append(child)
            incoming[child] += 1
        complete_time = [0] * (n+1)
        dq = deque()
        for child in range(1, n+1):
            if not incoming[child]:
                dq.append(child)
                complete_time[child] = time[child]
        while dq:
            parent = dq.popleft()

            for child in graph[parent]:
                complete_time[child] = max(complete_time[child], complete_time[parent]+time[child])
                incoming[child] -= 1

                if not incoming[child]:
                    dq.append(child)

        return max(complete_time)

        
