
for _ in range(int(input())):
    n, k = map(int, input().split())
    string = input()
    
    cnt_w = string[:k].count("W")
    mn = cnt_w 
    
    for b in range(1,n-k):
        if string[b] == "W":
            cnt_w += 1
            mn = min(mn, cnt_w)
        a = b-k+1
        if string[a-1] == "W":
            cnt_w -= 1
    print(mn)
