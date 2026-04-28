class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        color = [0] * numCourses
        order = []
        for course, pre in prerequisites:
            graph[pre].append(course)



        def dfs(node):
            
            if color[node] == 1:
                return False
            color[node] = 1
            

            for child in graph[node]:
                
                if color[child] != 2:
                    if not dfs(child):
                        return False

            color[node] = 2
            order.append(node)
            return True

        for node in range(numCourses):
            if color[node] != 0:
                continue
            if not dfs(node):
                return []
        
        return order[::-1]
        
        
        

