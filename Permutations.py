class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        k = len(nums)
        def fun(curr, used):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                    
                curr.append(nums[i])
                used.add(i)

                fun(curr,used)

                curr.pop()
                used.remove(i)
            
        
        fun([], set())
        return res
            
            
