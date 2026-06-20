class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dp(i, curr):
            if i == n:
                if curr == target:
                    return 1
                else:
                    return 0

            l = dp(i+1, curr+nums[i])
            r = dp(i+1, curr-nums[i])

            return l + r
        return dp(0, 0)



