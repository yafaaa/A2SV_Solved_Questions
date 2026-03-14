class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for ch in s:
            if ch != '*':
                l.append(ch)
            else:
                if l:
                    l.pop()
        return ''.join(l)
