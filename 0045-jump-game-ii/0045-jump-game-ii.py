class Solution:
    def jump(self, nums: List[int]) -> int:
        
        maxi_idx = 0
        my_end = 0
        ans = 0
        for i in range(len(nums) - 1):
            num = nums[i]
            maxi_idx = max(maxi_idx, i + num)
            if i == my_end:
                ans += 1
                my_end = maxi_idx
        return ans

        