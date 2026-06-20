class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache
        def dp(i, h):
            if i == n:
                return 0
            skip = dp(i+1, h)
            buy, sell = 0, 0
            if not h:
                buy = - prices[i] + dp(i+1, True)
            else:
                sell = prices[i] - fee + dp(i+1, False)
            
            return max(skip, buy, sell)
        
        return dp(0, False)

