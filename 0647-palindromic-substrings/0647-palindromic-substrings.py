class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        pal_memo = {}
        memo = {}
        def is_pal(i,j):

            if (i,j) in pal_memo:
                return pal_memo[(i,j)]
            if i >= j:
                return True

            if s[i] != s[j]:
                return False
            
            pal_memo[(i,j)] = is_pal(i+1, j-1)

            return pal_memo[(i,j)]
            

        def dp(i):
            ans = 1
            for j in range(i+1,n):
                if is_pal(i,j):
                    ans += 1
            return ans
            
        res = 0
        for i in range(n):
            res += dp(i)
        return res