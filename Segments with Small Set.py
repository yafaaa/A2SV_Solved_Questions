from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
a = 0
d = defaultdict(int)
mx = 0
ans = 0
for b in range(n):
    d[nums[b]] += 1
    while len(d.keys()) > k:
        d[nums[a]] -= 1
        if not d[nums[a]]:
            del d[nums[a]]
        a += 1
    ans += (b-a+1)
print(ans)
