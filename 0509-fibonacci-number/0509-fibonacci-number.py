class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            memo = {}
            if n == 1:
                return 1
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            memo[n] = fun(n-1) + fun(n-2)
            return memo[n]
        return fun(n)