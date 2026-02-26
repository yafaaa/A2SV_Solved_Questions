n , m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
a, b = 0, 0
ans = 0
while a<n and b<m:

    if l1[a] == l2[b]:
        ca, cb = 1, 1
        while a+1<n and l1[a] == l1[a+1]:
            ca += 1
            a += 1

        while b+1<m and l2[b] == l2[b+1]:
            cb += 1
            b += 1
        a += 1
        ans += (ca*cb)

    elif l1[a] > l2[b]:
        b += 1

    else:
        a += 1
print(ans)
