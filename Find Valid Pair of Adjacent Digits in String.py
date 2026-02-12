from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        d = Counter(s)

        for i in range(1, len(s)):
            v = d[s[i]]
            if int(s[i]) != v:
                continue
            if s[i] != s[i-1] and int(s[i-1]) == d[s[i-1]]:
                return f"{s[i-1]}{s[i]}"
        
        return f""
