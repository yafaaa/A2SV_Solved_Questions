from collections import defaultdict
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = defaultdict()
        d[0] = 1
        prefix = 0
        mn = 0 
        mx = float('-inf')
        for i in range(len(nums)):
            prefix += nums[i]
            mx = max(mx, prefix-mn)
            mn = min(mn, prefix)
        return mx
            

        
