class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s = list(s.split())
        n = len(p)
        
        if n != len(s):
            return False
        
        d = dict()
        seen = set()
        for i in range(n):
            if p[i] not in d:
                if s[i] in seen:
                    return False
                d[p[i]] = s[i]
                seen.add(s[i])

            elif d[p[i]] != s[i]:
                return False
        return True
            

                
