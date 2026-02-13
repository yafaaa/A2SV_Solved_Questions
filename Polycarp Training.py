n = int(input())
l = list(map(int, input().split()))
l.sort()
day = 1
for a in l:
    if a >= day:
        day += 1
print(day-1)
