class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(i, curr):
            
            if curr == n:
                return 1

            if curr > n or i ** x > n-curr:
                return 0

            skip = dp(i+1, curr)
            take = dp(i+1, curr+(i ** x))

            return (skip + take) % mod
            
        return dp(1, 0)