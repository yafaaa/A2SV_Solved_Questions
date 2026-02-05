from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        d = Counter(chars)
        for l in words:
            temp = d.copy()
            f = True
            for a in l:
                if a in temp:
                    temp[a]-=1
                    if temp[a]==0:
                        del temp[a]
                else:
                    f = False
                    break
            if f:
                total+=len(l)
        return total

