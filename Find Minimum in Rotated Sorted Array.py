class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 0
        left = 1
        right = len(nums)-1

        def fun(low):
            return nums[low] < nums[0]

        
        while left <= right:
            mid = (left+right) // 2

            if fun(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[ans]
        
