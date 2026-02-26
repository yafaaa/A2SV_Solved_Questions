
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    target = 0
    for i in range(1,n):
        target += abs(nums[i] - nums[i-1])
    
    res = []
    res.append(nums[0])
    
    for i in range(1,n-1):
        if not ((nums[i-1] <= nums[i] <= nums[i+1]) or (nums[i-1] >= nums[i] >= nums[i+1])):
            res.append(nums[i]) 
    
    res.append(nums[n-1])
    
    print(len(res))
    print(" ".join(map(str,res)))
            
        


