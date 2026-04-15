class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
        ans = 0

        def fun(n):
            cnt = 0
            for candy in candies:
                cnt += candy//n
            return cnt >= k
        
        while l <= r:
            m = (l+r)//2
            if fun(m):
                ans = m 
                l = m + 1
            else: 
                r = m - 1
        return ans
                
