class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res= []
        nums = [i+1 for i in range(n)]
        n = len(nums)
        def fun(curr, s):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(s,n):
                curr.append(nums[i])
                fun(curr, i+1)
                curr.pop()

        fun([], 0)
        return res
