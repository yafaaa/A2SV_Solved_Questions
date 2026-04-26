from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right

def a_n():
    return int(input())

def a_s():
    return input().strip()

def a_map():
    return map(int, input().split())

def a_nums():
    return list(map(int, input().split()))

n = int(input())
matrix = [[0]* n for _ in range(n)]

i,j = map(int, input().split())
qi,qj = i-1, j-1

i,j = map(int, input().split())
ki,kj = (i-1,j-1)

i,j = map(int, input().split())
ti, tj = (i-1,j-1)

for i in range(n):
    for j in range(n):
        if i == qi or j == qj:
            matrix[i][j] = 1
        if qi-qj == i - j:
            matrix[i][j] = 1
        if qi+qj == i + j:
            matrix[i][j] = 1

# for i in range(n):
#     print(matrix[i])

dq = deque([(ki,kj)])
visited = set((ki,kj))
direction = [(1,0), (-1,0), (0, 1), (0, -1), (1,1), (1,-1), (-1,-1), (-1,1)]

def inbound(nw_r,nw_c):
    return 0<= nw_r < n and 0<= nw_c < n

f = False
while dq:
    parent = dq.popleft()
    r,c = parent
    if r == ti and c == tj:
        f = True
        break

    for dr, dc in direction:
        nw_r = dr + r
        nw_c = dc + c

        if inbound(nw_r, nw_c) and (nw_r, nw_c) not in visited and matrix[nw_r][nw_c] != 1:
            visited.add((nw_r, nw_c))
            dq.append((nw_r, nw_c))


# matrix[ti][tj] = 2
# matrix[ki][kj] = 3
# for i in range(n):
#     print(matrix[i])

if f:
    print("YES")
else:
    print("NO")










