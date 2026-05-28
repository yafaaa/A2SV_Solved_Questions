class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}
        memo_pal = {}
        def is_pal(i,j):
            
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = is_pal(i+1, j-1)
            return memo[(i,j)]

            
            
        
        def dp(i):
            if i == n:
                return 0
            if is_pal(i, n-1):
                return 0
            if i in memo:
                return memo[i]
            cut = n
            for j in range(i,n):
                if is_pal(i,j):
                    cut = min(cut, 1 + dp(j+1)) 
            memo[i] = cut
            return cut
        
        return dp(0)

            