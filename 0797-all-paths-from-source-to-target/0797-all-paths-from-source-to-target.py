class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        dq = deque([[0]])
        result = []
        while dq:
            path = dq.popleft()
            last_node = path[-1]
            if last_node == target:
                result.append(path)
                continue

            for child in graph[last_node]:
                new_path = list(path) # deep copy
                new_path.append(child)
                dq.append(new_path)
        return result



