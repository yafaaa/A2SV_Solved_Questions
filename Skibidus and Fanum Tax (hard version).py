
def solve():
    n, m = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    nums2.sort()
    prev = float('-inf')

    debug = []
    for num in nums1:
        left, right = 0, m-1
        ans = num
        while left <= right:
            mid = (left+right)//2
            
            if nums2[mid]-num >= prev:
                if ans >= prev:
                    ans = min(ans, nums2[mid]-num)
                else:
                    ans = nums2[mid]-num
                right = mid - 1
            else:
                left = mid + 1
        if ans < prev:

            return "NO"
        
        prev = ans
    return "YES"
for _ in range(int(input())):
    print(solve())

    

    
