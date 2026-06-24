class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                return x

            if parent[x] == x:
                return x
        
            parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return True
            parent[rooty] = rootx

        for s in equations:
            if s[1] == "=":
                union(s[0], s[3])
        
        for s in equations:
            if s[1] == "!":
                if find(s[0]) == find(s[-1]):
                    return False
        return True


        

        
        
        

            