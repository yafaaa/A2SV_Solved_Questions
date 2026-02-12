
f = False
r, c = 0, 0
for i in range(5):
    row = list(map(int,input().split()))
    for j in range(5):
        if f:
            break
        if row[j] == 1:
            r, c = i, j
            f = True

print(abs(2-r) + abs(2-c))

        

