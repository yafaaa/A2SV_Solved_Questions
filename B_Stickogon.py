from collections import Counter
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    d = Counter(nums)
    cnt = 0
    for k, v in d.items():
        cnt += v//3
    print(cnt)