from typing import List
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we cannot split it into two equal integer subsets
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        @cache
        def dfs(i: int, current_target: int) -> bool:
            # Base Case 1: We found a subset that hits the target perfectly
            if current_target == 0:
                return True
                
            # Base Case 2: Out of bounds or target went negative
            if i >= len(nums) or current_target < 0:
                return False
            
            # Choice 1: Include the current number nums[i]
            # Choice 2: Exclude the current number nums[i]
            # If either choice leads to a True, return True
            return dfs(i + 1, current_target - nums[i]) or dfs(i + 1, current_target)
            
        return dfs(0, target)