class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = pow(10, 9) + 7        
        def fast_pow(b, e):
            if e == 0:
                return 1
            if b == 0:
                return 0
            if e < 0:
                b, e = 1/b, -e
            b %= mod
            if not e%2:
                return fast_pow(b*b, e//2) % mod
            else:
                return b * fast_pow(b*b, e//2) % mod
        
        m = n//2
        if not n%2:
            return (fast_pow(5,m) * fast_pow(4,m)) % mod
        else:
            return (fast_pow(5, m+1) * fast_pow(4,m)) % mod



