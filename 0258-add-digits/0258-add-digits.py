class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            s = 0
            while num:
                l = num % 10
                s += l
                num //= 10
            num = s
        return num
