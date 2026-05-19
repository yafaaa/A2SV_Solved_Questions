class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)

        for i in range(n-1, -1, -1):
            l = nums[i] + dp[i+2]
            r = dp[i+1]
            dp[i] = max(l, r)
        return dp[0]
            

        # memo = {}

        # def dp(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in memo:
        #         return memo[i]
        # return dp(0)
