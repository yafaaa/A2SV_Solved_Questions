class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mx = float('-inf')
        mn = float('inf')
        for num in nums:
            mx = max(mx,num)
            mn = min(mn, num)
        arr = [0] * (mx-mn+1)
        offset = -mn
        
        for num in nums:
            arr[num+offset] += 1
        cnt = 0
        for i in range(mx-mn, -1, -1):
            if arr[i]:
                cnt += arr[i]
                if cnt >= k:
                    return i-offset


