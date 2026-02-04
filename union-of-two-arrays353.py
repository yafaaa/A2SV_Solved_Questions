class Solution:    
    def findUnion(self, a, b):
        a.extend(b)
        l = sorted(set(a))
        return l
