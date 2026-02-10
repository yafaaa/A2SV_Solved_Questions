from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        dict_w = dict()
        dict_l = dict()
        res = []
        for w, l in matches:
            dict_w[w] = dict_w.get(w,0) + 1
            dict_l[l] = dict_l.get(l, 0) + 1
        a1 = sorted(dict_w.keys() - dict_l.keys())
        res.append(a1)
        a2 = sorted([k for k, v in dict_l.items() if v==1])
        res.append(a2)
        return res

        
