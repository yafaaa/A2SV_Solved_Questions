class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        def merge(l, r):
            nonlocal cnt
            if l == r:
                return [nums[l]]
            mid = (l+r)//2
            
            left_arr = merge(l, mid)
            right_arr = merge(mid+1, r)
            
            for num in left_arr:
                cnt += bisect_left(right_arr, math.ceil(num/2))
            
            return sorted(left_arr + right_arr)

        merge(0, len(nums)-1)
        return cnt