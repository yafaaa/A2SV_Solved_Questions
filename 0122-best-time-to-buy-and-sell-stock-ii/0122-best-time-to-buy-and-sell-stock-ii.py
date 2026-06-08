class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dp(i, hi):
            if i == n:
                return 0
            buy, sell = 0, 0
            if hi == 0:
                buy = -prices[i] + dp (i+1, 1)
            else:
                sell = prices[i] + dp(i+1, 0)

            skip = dp(i+1, hi)
            return max(skip, buy, sell)
        
        return dp(0, 0)