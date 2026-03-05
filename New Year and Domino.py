n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(input()))


pre_ver = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        pre_ver[i][j] = pre_ver[i-1][j] + pre_ver[i][j-1] - pre_ver[i-1][j-1] 
        if i-1 > -1:
             if mat[i][j] == "." and mat[i-1][j] == ".":
                 pre_ver[i][j] += 1

pre_hor = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    for j in range(m):
        pre_hor[i][j] = pre_hor[i-1][j] + pre_hor[i][j-1] - pre_hor[i-1][j-1] 
        if j-1 > -1:
             if mat[i][j] == "." and mat[i][j-1] == ".":
                 pre_hor[i][j] += 1


for _ in range(int(input())):
    row1, col1, row2, col2 = map(int, input().split())
    row1 -= 1
    col1 -= 1
    row2 -= 1
    col2 -= 1
    sub_hor = pre_hor[row2][col1] + pre_hor[row1-1][col2] - pre_hor[row1-1][col1]
    sub_ver = pre_ver[row1][col2] + pre_ver[row2][col1-1] - pre_ver[row1][col1-1]
    whole_hor = pre_hor[row2][col2]
    whole_ver = pre_ver[row2][col2]
    
    print(whole_ver-sub_ver + whole_hor-sub_hor)

