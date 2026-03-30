class Solution:
    def isSumString (self, s):
        f = [False] 
        def backtrack(p1, p2, start):
            p3 = p1 + p2
            
            if str(p3) == s[start:]:
                if p1<0 or p2 <0:
                    return
                return True 
            
            if len(s)>start and s[start] == '0':
                return
            
            
            t = ""
            
            for j in range(start, len(s)):
                if p1 == -1 or p2 == -1:
                    t += s[j] 
                    if backtrack(p2, int(t), j+1):
                        return True
                    continue
                t += s[j] 
                if int(t) == p3:
                    if backtrack(p2, int(t), j+1):
                        return True
                    
                if int(t) > p3:
                    return
        return True if backtrack(-1,-1, 0) else False
