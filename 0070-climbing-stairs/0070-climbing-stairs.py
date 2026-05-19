class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):

            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            l = dp(i+1)
            r = dp(i+2)
            memo[i] =  l + r
            return memo[i]
        return dp(0)