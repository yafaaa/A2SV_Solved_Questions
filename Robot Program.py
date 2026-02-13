

for _ in range(int(input())):
    n, p, k = map(int, input().split())
    string = input()

    move = 0
    for i in range(min(n,k)):
        p += 1 if string[i] == "R" else -1
        move += 1
        if p == 0:
            break
    else:
        print("0")
        continue
    first_move = move
    k -= move
    for i in range(min(n,k)):
        p += 1 if string[i] == "R" else -1
        k -= 1
        move += 1
        if p == 0:
            break
    else:
        print("1")
        continue
    m = move - first_move
    
    print(k//m + 2)


