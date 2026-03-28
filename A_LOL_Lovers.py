n = int(input())
string = input()
bl = string.count('L')
bo = string.count('O')
al,ao = 0, 0
idx = 0
for i in range(len(string)):
    ch = string[i]
    if ch == 'L':
        al += 1
        bl -= 1
    else:
        ao += 1
        bo -= 1
    if al != bl and ao != bo and i != len(string)-1:
        print(i+1)
        break

else:
    print(-1)