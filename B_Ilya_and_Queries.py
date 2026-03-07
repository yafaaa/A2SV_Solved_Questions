string = input()
n = len(string)
string = "0" + string
prefix = [0] * (n+1)
for i in range(1,n+1):
    prefix[i] += prefix[i-1] 
    if string[i] == string[i-1]:
        prefix[i] += 1
for _ in range(int(input())):
    l, r = map(int, input().split())
    print(prefix[r]-prefix[l])
    
    