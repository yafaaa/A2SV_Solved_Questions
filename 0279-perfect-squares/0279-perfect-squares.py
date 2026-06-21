class Solution:
    def numSquares(self, n: int) -> int:
        
        @cache
        def dp(remain):
            if remain == 0:
                return 0
            
            mn = float('inf')
            for i in range(1, int( sqrt(remain) ) + 1):
                mn = min(mn, 1 + dp(remain-(i * i)))
            return mn

        return dp(n)