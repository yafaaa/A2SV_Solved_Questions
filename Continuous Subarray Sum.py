from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        d[0] = -1
        prefix = 0
        cnt = 0
        for b in range(len(nums)):
            prefix += nums[b]
            t = prefix % k
            
            if t in d:
                if b-d[t] >= 2:
                    return True
            else:
                d[t] = b
                
        return False 
            
        
