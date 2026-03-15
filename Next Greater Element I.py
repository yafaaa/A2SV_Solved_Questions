from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        d = defaultdict(lambda :-1)
        stack = []

        for i in range(n):

            while stack and nums2[stack[-1]] < nums2[i]:
                d[nums2[stack.pop()]] = nums2[i]

            stack.append(i)
        
        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]
        return nums1
