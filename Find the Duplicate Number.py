class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        def move(idx):
            return nums[idx]
        
        slow = nums[0]
        fast = nums[slow]
        
        while nums[slow] != nums[fast]:
            slow = move(slow)
            fast = move(fast)
            fast = move(fast)
            
        slow = 0
        
        
        while nums[slow] != nums[fast]:
            slow = move(slow)
            fast = move(fast)

        return nums[fast]    
        
            




