class Solution:
    def knapsack(self, W, val, wt):
        
        memo = [[-1 for _ in range(W + 1)] for _ in range(len(wt) + 1)]
        def dp(i, avail_w):
            if i == len(wt):
                return 0
                
            if memo[i][avail_w] != -1:
                return memo[i][avail_w]
                
            l = dp(i+1, avail_w)
            
            r = 0
            if wt[i] <= avail_w:
                r = val[i] + dp(i+1, avail_w - wt[i])
            
            memo[i][avail_w] = max(l, r)
            return memo[i][avail_w]
        
        return dp(0, W)
