class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [inf] * n
        dp[-1] = 0
        for i in range(n - 2, -1, -1):
            for idx in range(i + 1, min(i + nums[i] + 1, n)):
                dp[i] = min(dp[i], 1 + dp[idx])

        return dp[0]




        