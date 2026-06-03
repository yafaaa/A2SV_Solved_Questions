class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}

        def dp(i, j):

            if i > j:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]
            
            l = piles[i] + dp(i+1, j)
            r = piles[j] + dp(i, j-1)

            
            memo[(i,j)] = max(l,r)
            return memo[(i,j)]

        return dp(0, n-1) > 0
            
            

