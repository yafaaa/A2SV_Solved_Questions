class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        area = 0
        while l < r:
            curr_area = min(height[l], height[r]) * (r-l)
            area = max(area,curr_area) 
            print(area)
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return area


            
