class Solution:
    def numDecodings(self, s: str) -> int:
        seen = set(str(i) for i in range(1, 27))
        n = len(s)
        @cache
        def dp(i):
            if i == n:
                return 1
            ways = 0
            for j in range(i,i+2):
                if s[i:j+1] in seen:
                    ways +=  dp(j+1)
            return ways
        
        return dp(0)

            
