class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = r

        def fun(cap):
            curr_d = 1
            curr_cap = 0

            for w in weights:
                if curr_cap + w > cap:
                    curr_d += 1
                    curr_cap = 0
                curr_cap += w
            return curr_d <= days
        
        while l <= r:
            m = (l+r)//2

            if fun(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


            

