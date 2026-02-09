from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)//3
        d = Counter(nums)
        res = []
        for k, v in d.items():
            if v>n:
                res.append(k)
        return res
