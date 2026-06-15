class Solution:
    def numDecodings(self, s: str) -> int:
        seen = set(str(i) for i in range(1, 27))
        n = len(s)
        @cache
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            ways = 0
            if s[i] in seen:
                ways += dp(i+1)
            if s[i:i+2] in seen:
                ways +=  dp(i+2)
            return ways
        
        return dp(0)

            
