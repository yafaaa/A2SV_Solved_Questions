class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(b) > len(a):
            a, b = b, a
            
        n = len(a)
        m = len(b)

        pb = m-1
        carry = 0
        res = []
        for i in range(n-1, -1, -1):
            if pb > -1:
                print(a[i], b[pb])
                ans = int(a[i]) + int(b[pb]) + carry
            else:
                ans = int(a[i]) + carry

            if ans < 2:
                res.append(str(ans))
                carry = 0
            elif ans == 2:
                res.append('0')
                carry = 1
            else:
                res.append('1')
                carry = 1
            pb -= 1

        if carry:
            res.append('1')

        return "".join(res[::-1])
                
