class Solution:
    def binstr(self, n):
        res = []

        v = 0
        def fun(curr, v):
            if len(curr) == n:
                res.append("".join(map(str,curr)))
                return
            
            curr.append(0)
            fun(curr, 0)
            curr.pop()
            
            curr.append(1)
            fun(curr, 1)
            curr.pop()
            
            
        
        fun([], 0)
        return res
        
