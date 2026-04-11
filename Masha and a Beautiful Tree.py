
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    def fun(arr):
        nonlocal cnt
        end = len(arr)
        if end == 1:
            return arr
        
        mid = (end-1)//2

        l = fun(arr[:mid+1])
        r = fun(arr[mid+1:])

        if l[0] < r[0]:
            return l + r
        else:
            cnt += 1
            return r + l

    curr = fun(nums)
    ans = [ i for i in range(1, n+1)]
    if curr != ans:
        print(-1)
    else:
        print(cnt)

for _ in range(int(input())):
    solve()  
