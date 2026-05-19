class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        pprev, prev = 1, 2 
        for i in range(3, n+1):
            curr = prev + pprev
            pprev = prev
            prev = curr
        return prev