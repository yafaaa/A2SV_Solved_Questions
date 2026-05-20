class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        memo = {}
        
        def dp(i, remain):
            if not remain:
                return 0
            if remain < 0 or i == n:
                return float('inf')
            if (i, remain) in memo:
                return memo[(i, remain)]
        
            memo[(i, remain)] = min(1 + dp(i, remain-coins[i]), dp(i+1, remain))
            return memo[(i, remain)]
        ans = dp(0, amount)
        return ans if ans != float('inf') else -1
