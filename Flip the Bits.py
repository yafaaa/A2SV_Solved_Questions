def fun():
    n = int(input())
    nums = list(map(int, input()))
    target = list(map(int, input()))
    cnt0, cnt1 = 0, 0

    for i in range(n-1):
        if nums[i] == 1:
            cnt1 += 1
        else:
            cnt0 += 1
        
        curr = (nums[i] == target[i])
        nxt = (nums[i+1] == target[i+1]) 
        if curr != nxt and cnt0 != cnt1:
                return f"NO"
    cnt0 += 1 if not nums[-1] else 0
    if (nums[-1]!= target[-1]) and (cnt0 != n-cnt0):
        return f"NO"
    return f"YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        print(fun())
