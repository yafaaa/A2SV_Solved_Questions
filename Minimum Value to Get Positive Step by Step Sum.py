class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = mn = nums[0]
        
        for i in range(1,len(nums)):
            prefix += nums[i]
            mn = min(mn, prefix)
        return 1 if mn > 0 else abs(mn)+1
