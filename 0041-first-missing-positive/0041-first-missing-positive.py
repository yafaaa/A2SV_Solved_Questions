class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            its_place = nums[i]-1

            if 0<= its_place < n and nums[i] != nums[its_place]: #still O(n)
                nums[i], nums[its_place] = nums[its_place], nums[i]
            else: 
                i += 1
        
        for idx in range(n):
            if nums[idx] != idx+1:
                return idx+1
        return n+1
            
            
            