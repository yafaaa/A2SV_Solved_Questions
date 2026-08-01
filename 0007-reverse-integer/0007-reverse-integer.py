class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        ss = ""
        if not x:
            return x
        while num > 0:
            s = num % 10
            num = num // 10
            ss += str(s)
        res = -int(ss) if x < 0 else int(ss)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res