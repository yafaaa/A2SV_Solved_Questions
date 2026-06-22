class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = {i:i for i in range(n)}
        rank = [0] * n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                elif rank[rooty] > rank[rootx]:
                    parent[rootx] = rooty
                else:
                    parent[rooty] = rootx
                    rank[rootx] += 1
        
        for a, b in pairs:
            union(a,b)

        group = defaultdict(list)

        for child, prent in parent.items():
            group[find(child)].append(child)

        res = list(s)

        for lst in group.values():
            chars = sorted(res[i] for i in lst)
            for idx, char in zip(sorted(lst), chars):
                res[idx] = char

        return "".join(res)
        
            
