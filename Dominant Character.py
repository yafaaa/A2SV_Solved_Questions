from collections import Counter
for _ in range(int(input())):
    n = int(input())
    string = input()
    lst_idx_a = []
    for i in range(n):
        if string[i] == "a":
            lst_idx_a.append(i)
    minn = n+1
    for i in range(1,len(lst_idx_a)):
        b, a = lst_idx_a[i], lst_idx_a[i-1]
        if b-a+1>=5:
            continue
        d = Counter(string[a:b+1])
        if 2>d["b"] and 2>d["c"] :
            minn = min(minn, b - a +1)
        elif i>1:
            b, a = lst_idx_a[i], lst_idx_a[i-2]
            if b-a+1>=8:
                continue
            d = Counter(string[a:b+1])
            if 3>d["b"] and 3>d["c"]:
                minn = min(minn, b - a +1)
            
    
    if minn == n+1:
        print(-1)
    else: 
        print(minn)
    
