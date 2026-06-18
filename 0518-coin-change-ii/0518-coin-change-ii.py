class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def dp(i, remain):
            if remain == 0:
                return 1
            if remain < 0 or i == n:
                return 0

            take = dp(i, remain-coins[i])
            skip = dp(i+1, remain)

            return take+skip
        return dp(0, amount)
