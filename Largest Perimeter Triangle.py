class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-1,1,-1):
            if nums[i] < nums[i-1] + nums[i-2]:
                res = max(res, nums[i]+nums[i-1]+nums[i-2])
                break
        return res
