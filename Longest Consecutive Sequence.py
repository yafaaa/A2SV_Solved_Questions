class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxx = 0
        cut_len = len(nums)//2
        
        for num in nums:
            cnt = 1
            if num-1 not in seen and num+1 in seen:        
                while num+1 in seen:
                    cnt += 1
                    num += 1
            maxx = max(maxx, cnt)
            if maxx > cut_len:
                break
        
        return maxx
        

        




            
