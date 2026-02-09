class Solution:
    def intToRoman(self, num: int) -> str:
        string = str(num)
        n = len(string)
        res = []
        d = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
        }
        for i in range(n):
            zero = n - (i+1)
            temp = int(string[i] + "0"*zero)
            lead = int(string[i])
            if temp >=1000:
                res.append(d[1000]*lead)
            elif lead == 4 or lead == 9:
                res.append(f"{d[10**zero]}{d[(lead+1)*(10**zero)]}")
            elif lead>=5:
                res.append(f"{d[5*(10**zero)]}{d[(10**zero)]*(lead-5)}")
            else:
                res.append(d[10**zero]*lead)
        return "".join(res)


                
