class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        def fun(l,r):
            m = (l+r)//2

            if l>r:
                return -1

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                return fun(l, m-1)
            else:
                return fun(m+1, r)
        return fun(l,r)
