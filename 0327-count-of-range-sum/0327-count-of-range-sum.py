class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])
        
    
        cnt = 0
        def merge(l, r):
            nonlocal cnt
            if l == r:
                return [prefix[l]]
            
            mid = (l + r) // 2
            left_half = merge(l, mid)
            right_half = merge(mid + 1, r)
            
            # prefix_sums[j] - upper <= prefix_sums[i] <= prefix_sums[j] - lower
            for pj in right_half:
                high = bisect_right(left_half, pj - lower)
                low = bisect_left(left_half, pj - upper)
                cnt += (high - low)
            
            return sorted(left_half + right_half)

        merge(0,len(prefix)-1)

        return cnt


        
