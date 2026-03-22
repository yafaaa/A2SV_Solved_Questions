def fun():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    m = nums[-1]
    if m <= 25:
        return 0
    seen = set(nums)
    cnt =0 
    return m-25
if __name__ == "__main__":
    print(fun())