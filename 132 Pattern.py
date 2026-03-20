class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        c = float('-inf')  

        for num in reversed(nums):
            if num < c:
                return True  
            while stack and stack[-1] < num:
                c = stack.pop()  
            stack.append(num)  
        
        return False


        
