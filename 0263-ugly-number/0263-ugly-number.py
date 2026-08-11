class Solution:
    def isUgly(self, n: int) -> bool:
        prime = [2, 3, 5]
        def fun(num):
            if num == 1 :
                return True
            if not num:
                return False
            for div in prime:
                if not num % div:
                    return fun(num//div)
            return False
        return fun(n)
                