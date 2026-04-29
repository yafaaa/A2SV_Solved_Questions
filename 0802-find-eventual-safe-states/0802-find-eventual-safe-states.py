class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0]*n
        ans = []

        def dfs(node):
            nonlocal ans
            if visited[node] == 1:
                return False
            visited[node] = 1
            
            for child in graph[node]:
                if visited[child] != 2:
                    if not dfs(child):
                        return False

            visited[node] = 2
            ans.append(node)
            return True
            
        
        for i in range(n):
            if  not visited[i] :
                dfs(i)
        
        ans.sort()
        return ans
# Standard way
# n = len(graph)
# state = [0] * n  # 0: unvisited, 1: visiting, 2: safe

# def dfs(node: int) -> bool:
# if state[node] != 0:
# return state[node] == 2  # 2 = safe, 1 = cycle/unsafe

# state[node] = 1  # mark as currently visiting

# for child in graph[node]:
# if state[child] == 1 or not dfs(child):
#     return False  # cycle detected or leads to unsafe node
    
# state[node] = 2  # all children are safe -> this node is safe
# return True

# return [i for i in range(n) if dfs(i)]
            