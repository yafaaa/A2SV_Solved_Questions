for _ in range(int(input())):
    n, m = map(int, input().split())
    if n ==m:
        print("YES")
        continue
    def fun(a):
        if a%3:
            return 0
        t = a//3
        l = t*2
        r = t
        if l == m:
            return 1
        if r == m:
            return 1
        return fun(l) + fun(r)
    res = fun(n)
    if res:
        print("YES")
    else:
        print("NO")