class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        try:
            res.append(nums.index(target))
            t = res[0] + 1
            n = len(nums)
            while t < n:
                if nums[t] == target:
                    res.append(t)
                else:
                    break
                t += 1
            return res
        except Exception as e:
            return res
