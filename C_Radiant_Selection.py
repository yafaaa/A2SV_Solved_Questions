import math
for _ in range(int(input())):
    k = int(input())

    l = 1
    r = k*2
    ans = k * 2

    def fun(n):
        return n - int(math.isqrt(n)) >= k
    
    while l<= r:
        m = (l+r)//2
        if fun(m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)

