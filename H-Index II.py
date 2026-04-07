class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)
        ans = l

        def fun(m):
            cnt = 0
            for c in citations:
                if c >= m:
                    cnt += 1
            return cnt >= m

        while l <= r:
            m = (l+r)//2

            if fun(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
