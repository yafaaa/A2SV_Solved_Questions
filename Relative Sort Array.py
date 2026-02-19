class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        res = []
        for a in arr2:
            res.extend([a]*d[a])
            del d[a]
        
        for a in sorted(d.keys()):
            res.extend([a]*d[a])
        return res
