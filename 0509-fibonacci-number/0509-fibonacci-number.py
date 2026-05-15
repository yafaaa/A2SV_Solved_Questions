class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        pprev, prev = 0, 1
        for i in range(2, n+1):
            cur = prev + pprev
            pprev = prev
            prev = cur
        return prev
    