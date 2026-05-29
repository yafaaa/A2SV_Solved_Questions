class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dp(i, hold):
            if i >= n:
                return 0

            if (i, hold) in memo:
                return memo[(i, hold)]

            skip = dp(i+1, hold)

            if not hold:
                trade = -prices[i] + dp(i+1, 1)
            else:
                trade = prices[i] + dp(i+2, 0)
            
            memo[(i, hold)] = max(trade,skip)
            return memo[(i, hold)]
        return dp(0,0)
        