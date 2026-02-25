class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        n = len(s)
        for i, ch in enumerate(s):
            d[ch] = i
        res = []
        seek = 0
        p = 0
        cnt = 0
        for p in range(n):
            seek = max(seek,d[s[p]])
            cnt += 1
            if p == seek:
                res.append(cnt)
                cnt = 0
            
        return res



