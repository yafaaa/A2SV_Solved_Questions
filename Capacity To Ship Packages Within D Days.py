class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def fun(cap):
            cnt = 1
            curr = 0
            mx = float('inf')
            for w in weights:
                if curr+w >cap:
                    cnt += 1
                    mx = max(curr, mx)
                    curr = 0
                
                curr += w

                if cnt > days:
                    break
            if cnt == days:
                mx = max(curr, mx)
                return mx
            return float('inf')

        while l<=r:
            m = (l+r)//2
            v = fun(m) 
            if v 
                


