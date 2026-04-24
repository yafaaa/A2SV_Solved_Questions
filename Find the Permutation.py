
for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input())))
    ans = [1]
    for i in range(2, n+1):
        
        for j, num in enumerate(ans):
            if not matrix[i-1][num-1]:
                ans = ans[:j] + [i] +ans[j:]
                break
        else:
            ans.append(i)
    
    print(*ans)



        



