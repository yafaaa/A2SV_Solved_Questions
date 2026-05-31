class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        memo = {}
        def dp(i,j):

            if i == n:
                return len(word2[j:])
            
            if j == m:
                return len(word1[i:])
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i] != word2[j]:

                replace = 1 + dp(i+1 ,j+1)
                delete = 1 + dp(i+1, j)
                insert = 1 + dp(i, j+1)

                ans = min(replace, delete, insert)

            else:
                ans = dp(i+1, j+1)

            memo[(i,j)] = ans
            return ans
        return dp(0,0)
                

