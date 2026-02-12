class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        d = dict()
        m = 0
        for r in responses:
            for s in set(r):
                d[s] = d.get(s, 0) + 1
                if d[s]>m:
                    m = d[s]
        res = []
        for k, v in d.items():
            if v == m:
                res.append(k)
        res.sort()
        return res[0]
            


        
