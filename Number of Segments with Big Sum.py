n, s = map(int, input().split())
nums = list(map(int, input().split()))
a = 0
curr_s = 0
ans = 0
for b in range(n):
    curr_s += nums[b]
    if curr_s < s:
        continue
    while curr_s-nums[a] >= s:
        curr_s -= nums[a]
        a += 1
    ans += a+1
    
print(ans)

    




























    
