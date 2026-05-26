class Solution:
    def inversionCount(self, arr):
        
        def merge(left, right):
            merged = []
            i = j = 0
            count = 0
            
            while i < len(left) and j < len(right):
                
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
        
        def merge_sort(arr):
            
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr)//2
            left, lcnt = merge_sort(arr[:mid])
            right, rcnt = merge_sort(arr[mid:])
            
            merged, cnt = merge(left, right)
            
            return merged, lcnt + cnt + rcnt
        
        _, ans = merge_sort(arr)
        return ans
