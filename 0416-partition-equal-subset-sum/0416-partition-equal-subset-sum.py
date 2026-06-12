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
                
            take = dp(i+1, curr+nums[i])
            if take:
                return True

            skip = dp(i+1, curr)

            return take or skip
        return dp(0, 0)