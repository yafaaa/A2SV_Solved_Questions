class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i >= n-1:
                return True
            
            for j in range(nums[i], 0, -1):
                if dp(i+j):
                    return True
            return False
        return dp(0)

            