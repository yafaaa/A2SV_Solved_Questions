class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right):
            if left > right:
                return 0
            pick_left = nums[left] - solve(left + 1, right)
            pick_right = nums[right] - solve(left, right - 1)
            return max(pick_left, pick_right)
        
        result = solve(0, len(nums)-1)
        return result >= 0  
