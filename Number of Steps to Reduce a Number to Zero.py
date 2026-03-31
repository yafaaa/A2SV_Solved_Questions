class Solution:
    def numberOfSteps(self, num: int) -> int:
        def fun(n, r):
            if n == 0:
                return r
            
            if not n%2:
                return fun(n//2, r+1)
            else:
                return fun(n-1, r+1)
        return fun(num, 0)
    
