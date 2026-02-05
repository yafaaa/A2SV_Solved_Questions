from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        res = []
        for p in paths:
            direct, *files = p.split()
            for f in files:
                name, *k = f.split("(")
                k=k[0][:-1]
                k="".join(k)
                d[k].append(f"{direct}/{name}")
        return [v for v in d.values() if len(v)>1]


        
