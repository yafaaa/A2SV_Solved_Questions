
for _ in range(int(input())):
    n , k = list(map(int, input().split()))
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    
    l.sort(key= lambda x : x[2])
    
    for l, r, real in l:
        if real <= k:
            continue
        if l<=k<=r:
            k = real
    print(k)
    
