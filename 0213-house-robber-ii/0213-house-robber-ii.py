class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i, f):
            if i >= n:
                return 0    
            take = 0
            if i == 0:
                take = nums[i] + dp(i+2, 1)
            elif i == n-1:
                if not f:
                    take = nums[i] + dp(i+2,f)
            else:
                take = nums[i] + dp(i+2,f)

            skip = dp(i+1,f)

            return max(take, skip)
        return dp(0, 0)