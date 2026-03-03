from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
d = defaultdict(int)
a = 0
mx = float('-inf')
idx_l = 0
for b in range(n):
    d[nums[b]] += 1
    if len(d.keys()) > k:
        d[nums[a]] -= 1
        if not d[nums[a]]:
            del d[nums[a]]
        a += 1
    if b-a+1 > mx:
        idx_l = a+1
        idx_r = b+1
        mx = b-a+1
print(idx_l, idx_r)
