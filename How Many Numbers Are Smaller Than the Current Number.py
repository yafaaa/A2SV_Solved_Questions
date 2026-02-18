class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = dict()
        for i, a in enumerate(sorted(nums)):
            if a in d:
                continue
            d[a] = i
        for i in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums
