class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        c = 0
        a = len(num1)-1
        res = ""
        for b in reversed(num2):
            curr = int(b) + c
            curr += int(num1[a]) if a > -1 else 0
            res += str(curr % 10)
            a -= 1
            c = 1 if curr > 9 else 0
        if c:
            res += str(c)
        return res[::-1]