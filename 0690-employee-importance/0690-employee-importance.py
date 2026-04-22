"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = defaultdict(list)
        
        for i in range(len(employees)):
            d[employees[i].id] = [employees[i].importance, employees[i].subordinates]

        cnt = 0
        visited = set()
        def dfs(target):
            nonlocal cnt
            importance, subordinate = d[target]
            cnt += importance            

            for t in subordinate:
                if t not in visited:
                    visited.add(t)
                    dfs(t)
        dfs(id)
        return cnt


            