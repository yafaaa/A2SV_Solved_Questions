class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}

        def dp(i, j, f):

            if i > j:
                return 0

            if (i,j,f) in memo:
                return memo[(i,j,f)]
            
            l = piles[i]*f + dp(i+1, j, f*-1)
            r = piles[j]*f + dp(i, j-1, f*-1)

            
            memo[(i,j,f)] = max(l,r) if f == 1 else min(l,r)
            return memo[(i,j,f)]
        ans = dp(0, n-1, 1)
        return ans > 0
            
            

