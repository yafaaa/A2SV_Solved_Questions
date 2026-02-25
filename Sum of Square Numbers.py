class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        if n**2 == c:
            return True
        l = [a**2 for a in range(1,n+1)]
        a, b = 0, len(l)-1
        
        while a <= b:
            if l[a]+l[b] < c:
                a += 1
            elif l[a]+l[b] > c:
                b -= 1
            else:
                return True
        return False


            
