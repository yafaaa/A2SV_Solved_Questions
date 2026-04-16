class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            its_place = abs(nums[i])-1
            if nums[its_place] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[its_place] = - nums[its_place]

        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
                break
        return ans
