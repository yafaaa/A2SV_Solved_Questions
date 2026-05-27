class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        def get_avg(i, j):
            total = prefix[j+1] - prefix[i]
            return total/(j-i+1)

        n = len(nums)
        memo = {}
        
        def dp(i, rk):
            if i == n:
                return 0
            if rk == 1:
                return get_avg(i, n-1)
            if (i, rk) in memo:
                return memo[(i, rk)]
            avg = 0.0
            for j in range(i, n-rk+1): 
                avg = max(avg, get_avg(i,j) + dp(j+1, rk-1))
            memo[(i, rk)] = avg
            return memo[(i, rk)]
        return dp(0, k)