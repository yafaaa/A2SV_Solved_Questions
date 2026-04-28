class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        prequist = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            prequist[course] += 1

        dq = deque([c for c in range(numCourses) if not prequist[c]])
        ans = []
        while dq:
            pre = dq.popleft()
            ans.append(pre)
            for course in graph[pre]:
                prequist[course] -= 1

                if not prequist[course]:
                    dq.append(course)
        if len(ans) != numCourses:
            return []
        return ans

