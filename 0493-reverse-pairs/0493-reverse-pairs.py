class Solution:
    def reversePairs(self, nums: List[int]) -> int:
            
        def merge(left, right):
            
            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
            
            # merge, this can be replaced by return sorted(right + left)

            # merged = []
            # i = j = 0
            # while i < len(left) and j < len(right):
            #     if left[i] <= right[j]:
            #         merged.append(left[i])
            #         i += 1
            #     else:
            #         merged.append(right[j])
            #         j += 1
            # merged.extend(left[i:])
            # merged.extend(right[j:])
            merged = sorted(left + right)
            
            return merged, count
        
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, lcnt = merge_sort(nums[:mid])
            right, rcnt = merge_sort(nums[mid:])
            merged, count = merge(left, right)
            return merged, lcnt + count + rcnt
            

        
        _, ans = merge_sort(nums)
        return ans