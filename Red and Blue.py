for _ in range(int(input())):
    n = int(input())
    ln = list(map(int, input().split()))
    m = int(input())
    lm = list(map(int, input().split()))
    mx = ln[0]
    for i in range(1,n):
        ln[i] += ln[i-1]
        mx = max(ln[i],mx)
    ans = max(0,mx)
    mx = lm[0]
    for i  in range(1,m):
        lm[i] += lm[i-1]
        mx = max(lm[i], mx)
    ans += mx if mx >0 else 0
    print(ans if ans >0 else 0)

    
