class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        n = len(s)
        summ = 0
        i = 0
        while i<n:
            if i+1 < n and s[i] in "IXC" and d[s[i+1]]>d[s[i]]:
                    summ +=d[s[i+1]] - d[s[i]]
                    i += 2
            else:
                summ += d[s[i]]
                i += 1
        return summ
                
            

            
