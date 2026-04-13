class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def fun(arr, i):
            if len(arr) >= 2:
                ans.append(arr[:])
                    
            seen = set()    
            for i  in range(i, len(nums)):
                if not arr or arr[-1] <= nums[i] :
                    if nums[i] not in seen:
                        arr.append(nums[i])
                        seen.add(nums[i])
                        fun(arr, i+1)
                        arr.pop()

            

        fun([],0)
        return ans
