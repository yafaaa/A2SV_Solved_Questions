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
    l, s = a_map()
    ss = s
    
    if s > 9 * l:
        return "-1 -1"
    
    if not s and l > 1:
        return "-1 -1" 
    
    num = []
    for _ in range(l):
        mx = min(9, s)
        num.append(mx)
        s -= mx
    lg = "".join(list(map(str, num)))
    s = ss
    num = []
    if s == 0:
        num.append(0)
    else:
        for i in range(l):
            rm_l = l - (i+1)
            lft_ovr = max(0, s - 9*(rm_l)) if i != 0 else max(1, s - 9*(rm_l))
            num.append(min(9,lft_ovr))
            s -= num[-1]

    sm = "".join(list(map(str, num)))
    return f"{sm} {lg}"
print(solve())