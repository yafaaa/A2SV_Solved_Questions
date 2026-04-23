# example below, replace it with your solution
from collections import defaultdict, deque

v, e = map(int, input().split())
s, desti = map(int, input().split())
d = defaultdict(list)
prev = {s : None}

for _ in range(e):
    e1, e2 = map(int, input().split())
    d[e1].append(e2)
    d[e2].append(e1)

dq = deque([s])
visited = set()
visited.add(s)
found = False
while dq:
    parent = dq.popleft()

    if parent == desti:
        found = True
        break
    for child in d[parent]:
        if child not in visited:
            dq.append(child)
            visited.add(child)
            prev[child] = parent

if not found:
    print(-1)
else:
    paz = []
    c = desti
    while c:
        paz.append(c)
        c = prev[c]
    print(len(paz)-1)
    print(*paz[::-1])

        

    

