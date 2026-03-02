from collections import defaultdict
class Solution:
    def atmost(self, nums, k):
        d = defaultdict(int)
        n = len(nums)
        a, cnt_k = 0, 0
        for b in range(n):
            d[nums[b]] += 1
            
            while len(d.keys()) > k:
                d[nums[a]] -= 1
                if not d[nums[a]]:
                    del d[nums[a]]
                a += 1
            cnt_k += b-a+1
        return cnt_k

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k-1) 
