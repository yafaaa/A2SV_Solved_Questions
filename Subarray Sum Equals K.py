from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        curr_s = 0
        cnt = 0 
        for i in range(n):
            curr_s += nums[i]
            target = curr_s - k
            if target in d:
                cnt += d[target]
            d[curr_s] += 1
        return cnt
        
        
        
        

        
            
        
