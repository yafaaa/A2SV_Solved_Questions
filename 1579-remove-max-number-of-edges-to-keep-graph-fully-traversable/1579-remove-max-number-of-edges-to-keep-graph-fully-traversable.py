class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.component = n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x
            self.component -= 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu_bob = DSU(n)
        dsu_alice = DSU(n)

        used = 0
        remove = 0

        for type_, x, y in edges:
            if type_ == 3:
                ub = dsu_bob.union(x, y)
                ua = dsu_alice.union(x, y)
                if ua  or ub:
                    used += 1
                else:
                    remove += 1

        for type_, x, y in edges:

            if type_ == 1:
                if dsu_alice.union(x, y):
                    used += 1
                else:
                    remove += 1
            elif type_ == 2:
                if dsu_bob.union(x, y):
                    used += 1
                else:
                    remove += 1
        
        if dsu_bob.component == 1 and dsu_alice.component == 1:
            return remove
        
        return -1

                    
                
            



        