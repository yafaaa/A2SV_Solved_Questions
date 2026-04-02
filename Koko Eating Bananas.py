class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def fun(k):
            cnt = 0
            m = 0
            for p in piles:
                cnt += math.ceil(p/k)

                if cnt >  h: ######
                    return False    

            # if cnt >  h:
            #     return False
            else:
                return True
        
        while l <= r:
            m = (l+r)//2

            if fun(m):
                r = m - 1
            else:
                l = m + 1
        return l

            

                    
