from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        cnt = 0
        
        for l in d.values():
            n = len(l)
            for i in range(n):
                for j in range(i+1,n):
                    if (l[i]*l[j])%k == 0:
                        cnt += 1
                    
        return cnt
                
