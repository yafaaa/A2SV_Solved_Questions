import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l = 0
        r = max(max(houses), max(heaters)) - min(min(houses), min(heaters))
        ans = r
        heaters.sort()

        def fun(r):
            for home in houses:
                i = bisect.bisect_left(heaters, home)

                right_d = heaters[i] - home if i < len(heaters) else float('inf')

                left_d = home - heaters[i-1] if i > 0 else float('inf')

                if min(right_d, left_d) > r:
                    return False
            return True
                
        
        while l <= r:
            m = (l+r)//2

            if fun(m):
                ans = m
                r = m-1
            else:
                l = m + 1
                
        return ans
                
            
