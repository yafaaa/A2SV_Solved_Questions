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
    names = []
    graph = [set() for _ in range(26)]
    incoming = [0] * 26
    for _ in range(n):
        string = a_s()
        names.append(string)

    def fun(word1, word2):
        i = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                u, v = ord(word2[i])-ord('a'), ord(word1[i])-ord('a')

                if u not in graph[v]:
                    graph[v].add(u)
                    incoming[u] += 1
                return
            i += 1
        if len(word1) > len(word2):
            return True
    for i in range(n-1):
        if fun(names[i], names[i+1]):
            return 'Impossible'

    dq = deque([i for i in range(26) if not incoming[i] ])

    ans = []
    while dq:
        parent = dq.popleft()
        ans.append(chr(parent + ord('a')))

        for child in graph[parent]:
            incoming[child] -= 1
            if not incoming[child]:
                dq.append(child)
    return "".join(ans) if len(ans)== 26 else 'Impossible'
print(solve())    



