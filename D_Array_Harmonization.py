
for _ in range(int(input())):
    n, _ = list(map(int, input().split()))
    nums_a = list(map(int, input().split()))
    nums_b = list(map(int, input().split()))

    nums_a.append(1)

    nums_a.sort()
    nums_b.sort()

    b = n-1
    count = 0
    for i in range(n-1, -1 , -1):
        if nums_b[b] > nums_a[i]:
            count += 1
            b -= 1

    print(n - count)



