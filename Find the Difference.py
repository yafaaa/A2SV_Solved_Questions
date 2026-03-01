class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(t)
        for ch in s:
            if ch in d:
                d[ch] -= 1
                if not d[ch]:
                    del d[ch]
        return "".join([k*v for k, v in d.items()])
