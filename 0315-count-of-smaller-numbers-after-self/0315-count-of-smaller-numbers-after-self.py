class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        def merge(l, r):

            if l == r:
                return [[nums[l], l]]
            
            mid = (l+r)//2

            left_arr = merge(l, mid)
            right_arr = merge(mid+1, r)

            for num, i in left_arr:
                idx = bisect_left(right_arr, [num, -inf])
                res[i] += idx
                
            return sorted(left_arr + right_arr)
        merge(0, len(nums)-1)
        return res
        