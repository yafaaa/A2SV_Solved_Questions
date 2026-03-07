from itertools import accumulate
n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix = list(accumulate([0] + nums))
mn = float('inf')
idx = 0
for b in range(k,n+1):
    a = b-k+1
    if prefix[b]-prefix[a-1] < mn:
        idx = a
        mn = prefix[b]-prefix[a-1]
print(idx)
