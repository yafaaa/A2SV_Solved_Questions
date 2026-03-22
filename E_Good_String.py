n = int(input())
string = input()
l = [string[0]]
f = -1
for ch in string:
    if f == 1:
        l.append(ch)
        f *= -1
        continue
    if f == -1 and ch != l[-1]:
        l.append(ch)
        f *= -1
ans = len(string) - len(l)
if len(l)%2:
    l.pop()
    ans += 1

print(ans)
print("".join(l))