class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        d1 = Counter(s1)
        d2 = Counter(s2)
        dt = d1.copy()
        dt.update(s2)
        n = len(s1)
        s1 = list(s1)
        s2 = list(s2)
        t = all(a%2 == 0 for a in dt.values())
        if not t:
            return -1
        c = 0

        for i in range(n):
            if s1[i] != s2[i]:
                avail = next((j for j in range(i+1,n) if s2[j] == s2[i] and s1[j] != s2[j]), None)
                if avail:
                    s2[avail] = s1[i]
                    d1[s2[i]] += 1
                    d1[s1[i]] -= 1
                    d2[s2[i]] -= 1
                    d2[s1[i]] += 1
                    c += 1
                    
                else:
                    temp = next((j for j in range(i+1, n) if s2[j] == s1[i] and s1[j] == s2[i]))
                    s1[temp] = s1[i]
                    c += 2
        return c
        
