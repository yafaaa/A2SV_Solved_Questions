from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a, b = 0, 0
        d = defaultdict(int)
        m = 0
        mx = 0
        for b in range(len(s)):
            d[s[b]] += 1
            mx = max(mx, d[s[b]])
            while (b-a+1) - (mx) > k:
                d[s[a]] -= 1
                a += 1
            m = max(m, b-a+1)
        return m

            
