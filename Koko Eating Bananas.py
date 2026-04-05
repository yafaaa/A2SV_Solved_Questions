class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        def fun(v):
            cnt = 0 
            for p in piles:
                cnt += math.ceil(p/v)
            return cnt <= h
        
        while l <= r:
            
            mid = (l+r)//2

            if fun(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
