class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left = 0
        right = m 

        total_left = (m+n+1)//2 # left+1 = right in odd cases

        while left <= right:
            mi = (left + right)//2

            mj = total_left - mi

            left1 = nums1[mi-1] if mi > 0 else float('-inf')
            right1 = nums1[mi] if mi < m else float('inf')
            left2 = nums2[mj-1] if mj > 0 else float('-inf')
            right2 = nums2[mj] if mj < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if not (m+n) % 2: #even
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = mi - 1
            else:
                left = mi + 1

        
            
            
