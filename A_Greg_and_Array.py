n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
op = [0]

for _ in range(m):
    op.append(list(map(int, input().split())))

m_prefix = [0] * (m+2)
for _ in range(k):
    a, b = map(int, input().split())
    m_prefix[a] += 1
    m_prefix[b+1] -= 1

for i in range(1,m+2):
    m_prefix[i] += m_prefix[i-1]

for i in range(1,m+1):
    op[i][2] *= m_prefix[i]

nums = [0] + nums + [0]

prefix = [0]* (n+2)
for a, b ,c in op[1:]:
    prefix[a] += c
    prefix[b+1] -= c

for i in range(2,n+2):
    prefix[i] += prefix[i-1]

for i in range(1, n+1):
    nums[i] += prefix[i] 
print(" ".join(map(str,nums[1:n+1])))