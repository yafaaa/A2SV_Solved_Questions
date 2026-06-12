class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2 
        @cache
        def dp(i, curr):
            
            if curr == target:
                return True
            
            if curr > target or i == n:
                return False

            return dp(i+1, curr+nums[i]) or dp(i+1, curr)
        return dp(0, 0)