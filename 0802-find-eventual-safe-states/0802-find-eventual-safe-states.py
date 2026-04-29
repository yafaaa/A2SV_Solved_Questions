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
            