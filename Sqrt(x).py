class Solution:
    def mySqrt(self, x: int) -> int:
        def fun(l, r):
            while l<=r:
                m = (l+r)//2
                curr = m*m
                if curr == x:
                    return m
                elif curr > x:
                    r = m-1
                else:
                    l = m+1
            return l-1
        return fun(0, x)
           
        
