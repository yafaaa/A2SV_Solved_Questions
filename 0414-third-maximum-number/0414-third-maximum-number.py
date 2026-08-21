class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l = sorted(set(nums), reverse=True)
        if len(l) < 3:
            return l[0]
        return l[2]