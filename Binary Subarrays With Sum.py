from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int) 
        d[0] = 1
        prefix = 0
        cnt = 0

        for b in range(len(nums)):
            prefix += nums[b]
            t = prefix - goal
            if t in d:
                cnt += d[t]
            d[prefix] += 1
        return cnt
            

        
        
