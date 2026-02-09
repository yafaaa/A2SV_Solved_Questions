from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        res = []
        s = sorted(d.items(), key=lambda a: -a[1])
        return [k for k, v in s[:k]]
        
