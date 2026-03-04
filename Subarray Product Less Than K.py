class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        a = 0
        curr_p = 1
        cnt = 0
        n = len(nums)

        for b in range(n):
            curr_p *= nums[b]
            while a<= b and curr_p >= k:
                curr_p = curr_p // nums[a]
                a += 1
                if a >= n:
                    return cnt
            if curr_p < k:
                cnt += b-a+1
        return cnt
