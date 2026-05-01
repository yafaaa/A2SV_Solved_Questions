import sys
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def a_n():
    return int(input())

def a_s():
    return input().strip()

def a_map():
    return map(int, input().split())

def a_nums():
    return list(map(int, input().split()))
n = a_n()
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child = a_map()
    graph[parent].append(child)
    graph[child].append(parent)

def bfs(node):
    dq = deque([(node, -1)])
    level = 0
    last_n = node
    while dq:
        lgth = len(dq)
        level += 1
        for _ in range(lgth):
            parent, par = dq.popleft()
            last_n = parent
            for child in graph[parent]:
                if child == par: continue
                dq.append((child, parent))

    return level-1, last_n

_, root = bfs(1)
ans, _ = bfs(root)
print(ans*3)



            
