diff = []
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
for i in range(1,n):
    diff.append(nums[i]-nums[i-1])
total = sum(diff)
diff.sort()
for i in range(k-1):
    total -= diff[-1]
    diff.pop()
print(total)
