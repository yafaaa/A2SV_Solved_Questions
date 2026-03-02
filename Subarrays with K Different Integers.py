from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        a, cnt_k, cntk_1 = 0, 0, 0

        for b in range(n):
            d[nums[b]] += 1
            
            while len(d.keys()) > k:
                d[nums[a]] -= 1
                if not d[nums[a]]:
                    del d[nums[a]]
                a += 1
            cnt_k += b-a+1
        d.clear()
        a = 0
        for b in range(n):
            d[nums[b]] += 1
            
            while len(d.keys()) > k-1:
                d[nums[a]] -= 1
                if not d[nums[a]]:
                    del d[nums[a]]
                a += 1
            cntk_1 += b-a+1
        
        return cnt_k - cntk_1

            

