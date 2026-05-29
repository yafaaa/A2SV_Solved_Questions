class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dp(i, b, c):
            if i == n:
                return 0
            if (i,b,c) in memo:
                return memo[(i,b,c)]
            l = float('-inf')
            if not b and not c:
                l = -prices[i] + dp(i+1, 1, 0)

            r = float('-inf')
            if b and not c:
                r = prices[i] + dp(i+1, 0, 1)
            m = dp(i+1, b, 0)
            
            memo[(i,b,c)] = max(l,r,m)
            return memo[(i,b,c)]
        return dp(0,0,0)
        