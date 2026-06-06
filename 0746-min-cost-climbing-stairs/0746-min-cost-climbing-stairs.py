class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i):
            if i >= n:
                return 0
            cst = cost[i] if i != -1 else 0
            take = cst + dp(i+1)
            take2 = cst + dp(i+2)

            return min(take, take2)
        return dp(-1)