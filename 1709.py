
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split())) 
    l2 = list(map(int, input().split()))
    res = []

    for i in range(n):
        if l2[i] < l1[i]:
            l1[i], l2[i] = l2[i], l1[i]
            res.append([3, i+1])
    
    
    for i in range(n-1, 0, -1):
        for j in range(i):
            if l1[j+1] < l1[j]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                res.append([1, j+1])
    l1 = l2
    
    for i in range(n-1, 0, -1):
        for j in range(i):
            if l1[j+1] < l1[j]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                res.append([2, j+1])
        
    
    print(len(res))
    for l in res:
        print(" ".join(map(str,l)))




