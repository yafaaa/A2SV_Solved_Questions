from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cnt, prefix = 0, 0
        for i in range(len(nums)):
            prefix += nums[i]
            t = prefix % k
            if t in d:
                cnt += d[t]
            d[t] += 1
        return cnt
