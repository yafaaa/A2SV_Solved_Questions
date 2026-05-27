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
            mid = (l+r) // 2
            left = merge(l, mid)
            right = merge(mid+1, r)

            for a in left:
                rank = bisect_left(right, a-diff) 
                ans += len(right)-rank
            
            return sorted(left + right)
        
        merge(0, len(arr)-1)        
        return ans


        