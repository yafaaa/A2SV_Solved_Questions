class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        arr = [0] * len(graph)
        
        for i in range(len(graph)):
            if arr[i]:
                continue

            arr[i] = 2
            dq = deque([i])
            while dq:
                parent = dq.popleft()
                
                for child in graph[parent]:
                    if arr[child] and arr[child] == arr[parent]:
                        return False

                    elif not arr[child]:
                        arr[child] = 1 if arr[parent] == 2 else 2
                        dq.append(child)

            
        return True


            
