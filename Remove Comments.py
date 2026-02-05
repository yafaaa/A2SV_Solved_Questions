class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        str_l = []
        f = True
        l = 0
        while l < len(source):
            s = 0
            n = len(source[l])
            while s<n:
                if f:
                    if (source[l][s]=='/' and s+1<n) and (source[l][s+1]=='/' or source[l][s+1]=='*'):
                        if source[l][s+1]=='/':
                            break
                        elif source[l][s+1]=='*':
                            f = False
                            s+=1
                        else:
                            str_l+=source[l][s]
                    else:
                        str_l+=source[l][s]
                else:
                    if (source[l][s]=='*' and s+1<n) and source[l][s+1]=='/':
                        f=True
                        s+=1
                s+=1
            if f and str_l:
                res.append("".join(str_l))
                str_l=[]
            l+=1
        return res
