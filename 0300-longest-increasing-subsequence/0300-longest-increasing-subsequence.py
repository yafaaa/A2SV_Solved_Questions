class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1 for i in range(n)]
        def dp(i):
            if memo[i] != -1:
                return memo[i]

            lgth = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    lgth = max(lgth, 1 + dp(j))
            memo[i] = lgth
            return memo[i]
        
        ans = 0 
        for i in range(n):
            ans = max(ans, dp(i))
        return ans