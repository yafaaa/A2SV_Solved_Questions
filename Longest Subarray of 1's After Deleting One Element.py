class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = 0
        s = 0
        m = 0
        for b in range(len(nums)):
            s += nums[b]
            while (b-a+1) - s >1:
                s -= nums[a]
                a += 1
            m  = max(m, b-a+1)
        return m-1

