class DSU:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:

            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]
                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        
        for r in range(n):
            for c in range(r+1, n):
                if isConnected[r][c] == 1:
                    dsu.union(r,c)
        return len([key for key, value in dsu.parent.items() if key == value])


            


        


            


        