class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i]-nums2[i])
        
        ans = 0

        def merge(l, r):
            nonlocal ans
            if l == r:
                return [arr[l]]
            
            mid = (l+r)//2

            left_arr = merge(l,mid)
            right_arr = merge(mid+1,r)
            
            for j in right_arr:
                idx = bisect_right(left_arr, j+diff)
                ans += idx
            return sorted(left_arr + right_arr)
        
        merge(0, len(arr)-1)
        return ans

