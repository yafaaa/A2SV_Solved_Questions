def solve():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
 
    width = 0
    for height_person in a:
        if height_person > h:
            width += 2
        else:
            width += 1
    print(width)
 
solve()