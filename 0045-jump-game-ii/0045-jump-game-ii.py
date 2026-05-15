class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        @cache
        def backtrack(i):

            if i == n-1:
            
                return 0
            mn = inf
            for idx in range(i + 1, min(i + nums[i] + 1, n)):
                mn = min(mn, 1 + backtrack(idx))
            return mn
        return backtrack(0)




        