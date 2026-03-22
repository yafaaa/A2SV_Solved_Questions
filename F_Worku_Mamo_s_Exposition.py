from collections import deque
n, k = map(int, input().split())
nums = list(map(int, input().split()))

a = 0
mx = deque()
mn = deque()
ans = []
m = 0
for b in range(n):
    while mn and nums[mn[-1]]>nums[b]:
        mn.pop()
    mn.append(b)

    while mx and nums[mx[-1]] < nums[b]:
        mx.pop()
    mx.append(b)

    while nums[mx[0]]-nums[mn[0]] > k:
        if mx and a == mx[0]:
            mx.popleft()
        if mn and a == mn[0]:
            mn.popleft()
        a += 1
    
    if nums[mx[0]]-nums[mn[0]] <= k:
        if m <b-a+1:
            ans = []
            m = b-a+1
        if m <= b-a+1:
            ans.append([a+1,b+1])

print(m, len(ans))

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
    

