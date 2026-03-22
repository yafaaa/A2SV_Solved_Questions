a, t = map(int, input().split())

def fun(a, t):
    if a > t:
        return 0
    if a == t:
        return [t]
    l = a * 2
    r = (a*10) + 1
    rl = fun(l,t)
    rr = fun(r,t)
    if rl:
        return [l]+rl
    if rr:
        return [r] + rr
    
res = fun(a, t)
if res:
    print("YES")
    print(len(res))
    res = res[:-1]
    print(a, *res)
else:
    print("NO")