class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, a in enumerate(nums):
            if a in d:
                return [d[a],i]
            com = target - a
            d[com] = i
