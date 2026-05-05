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


def solve():
    n = a_n()
    nums = a_nums()
    graph = [[] for i in range(n+1)]
    incoming = [0] * (n+1)

    for i in range(len(nums)):
        parent, child = i+1, nums[i]
        graph[parent].append(child)
        incoming[child] += 1

    dq = deque([i for i in range(1,n+1) if not incoming[i]])
    cnt = 0
    while dq:
        lgth = len(dq)
        cnt += 1

        for _ in range(lgth):
            parent = dq.popleft()

            for child in graph[parent]:
                incoming[child] -= 1
                if not incoming[child]:
                    dq.append(child)

    return cnt+2

for _ in range(a_n()):
    print(solve())
