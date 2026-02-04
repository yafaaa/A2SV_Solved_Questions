#User function Template for python3
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        set_b = set(b)
        d1 = dict()
        d2 = dict()
        for e in a:
           if e in set_b:
               d1[e] = d1.get(e, 0)+1
        for e in b:
            d2[e] = d2.get(e, 0)+1
        if len(d1.keys()) != len(d2.keys()):
            return False
        for k,v in d1.items():
            if v<d2[k]:
                return False
        return True
        
    
    
    
