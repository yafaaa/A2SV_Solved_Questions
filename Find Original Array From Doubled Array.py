from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 != 0:
            return []
        res = []
        dict_odd = defaultdict(lambda : [0, 0])
        
        for num in changed:
            if num%2 != 0:
                l = dict_odd[num]
                l[0] += 1
                l[1] += 1
        
        changed.sort()

        for num in changed:
            if num%2 == 0:
                in_half = num//2
                if in_half in dict_odd and dict_odd[in_half][0]>=1:
                    dict_odd[in_half][0] -= 1
                else:
                    l = dict_odd[num]
                    l[0] += 1
                    l[1] += 1
    
        
        for k, l in dict_odd.items():
            if l[0] != 0:
                return []
            while l[1]:
                res.append(k)
                l[1] -= 1
        return res



        

            
        

