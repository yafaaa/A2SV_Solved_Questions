class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        res = [0]*n
        for i, idx in enumerate(indices):
            res[idx]=s[i]
        return "".join(res)
