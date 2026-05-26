class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, right):
        
            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
        
            # merge
            merged = sorted(left + right)
            return merged, count
    
    
        def merge_sort(l, r):
            if l == r:
                return [nums[l]], 0
            
            mid = (l + r) // 2
            left, lcnt = merge_sort(l, mid)
            right, rcnt = merge_sort(mid+1, r)
            merged, count = merge(left, right)
            return merged, lcnt + count + rcnt
            

        
        _, ans = merge_sort(0, len(nums)-1)
        return ans