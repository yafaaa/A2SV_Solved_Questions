def fun():
    n, k = map(int, input().split())
    num = list(input())
    nums =  [ord(ch)-96 for ch in num]
    nums.sort()
    
    l = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i]-l[-1] > 1:
            l.append(nums[i])
    return sum(l[:k]) if len(l) >= k else -1
if __name__ == "__main__":
    print(fun())
















