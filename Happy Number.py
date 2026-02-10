class Solution:
    def isHappy(self, n: int) -> bool:
        prev_list = list(str(n))
        seen = set()
        while True:
            summ = 0
            for s in prev_list:
                a = int(s)
                summ +=  (a ** 2)
            if summ == 1:
                return True
            if summ in seen:
                return False
            seen.add(summ)
            prev_list = list(str(summ))
            
