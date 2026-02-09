from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        dict_s = Counter(s)
        dict_t = Counter(t)
        c = 0
        for k, v in dict_s.items():
            if k not in dict_t:
                c+=v
            elif v > dict_t[k]:
                c+=(v-dict_t[k])
            
        return c



        
