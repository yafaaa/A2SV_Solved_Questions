from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * (n)
        nums.sort()

        for l, r in requests:
            prefix[l] += 1
            if r+1 < n:
                prefix[r+1] -= 1
        
        for i in range(1,n):
            prefix[i] += prefix[i-1]
        
        res = 0
        for i, val in enumerate(sorted(prefix)):
            res += val * (nums[i])

        return res % (10**9 + 7)
        
        

        

        
