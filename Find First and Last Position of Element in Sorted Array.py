class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        if not nums:
            return [-1, -1]
        def low():
            l = 0
            r = len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]>=target:
                    r = m
                else:
                    l = m+1
            return l

        def up():
            l = 0
            r = len(nums)
            while l<r:
                m = (l+r)//2
                if nums[m]>target:
                    r = m
                else:
                    l = m+1
            return l
                
        res = []
        first = low()
        if first >= len(nums) or nums[first] != target:
            return [-1, -1]
        last = up()-1
        res.append(first)
        res.append(last)
        
        
        return res
