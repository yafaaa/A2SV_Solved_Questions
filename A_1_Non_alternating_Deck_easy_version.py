
for  _ in range(int(input())):
    n = int(input())
    cnt = 0
    a, b= 0, 0
    while n > 0:
        for _ in range(2):
            m = min(cnt, n)
            a += m
            cnt += 1
            n -= m
            if n == 0:
                break
        
        for _ in range(2):
            m = min(cnt, n)
            b += m
            cnt += 1
            n -= m
            if n == 0:
                break
    print(f"{a} {b}")


    




