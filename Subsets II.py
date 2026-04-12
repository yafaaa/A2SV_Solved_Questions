class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()
        def fun(arr, i):
            if i == len(nums):
                curr_s = "".join(map(str,arr))
                if curr_s not in seen:
                    ans.append(arr[:])
                    seen.add(curr_s)
                return

            fun(arr, i+1)
            arr.append(nums[i])
            fun(arr, i+1)
            arr.pop()

            
        fun([],0)
        return ans


            

