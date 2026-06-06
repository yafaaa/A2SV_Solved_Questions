class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        mx = max(nums)
        @cache
        def dp(num):
            
            if num > mx:
                return 0
            
            take = (num*freq[num]) + dp(num+2)
            skip = dp(num+1)

            return max(take, skip)
        return dp(1)
            

        