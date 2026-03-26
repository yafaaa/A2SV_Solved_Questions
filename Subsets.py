class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def fun(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            fun(i+1, curr)

            curr.pop()
            fun(i+1, curr)
        fun(0, [])
        return res
