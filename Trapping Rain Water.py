class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        next_g = [0] * n   
        prev_g = [0] * n   
        
        
        prev_g[0] = height[0]
        for i in range(1, n):
            prev_g[i] = max(prev_g[i-1], height[i])
        
        
        next_g[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            next_g[i] = max(next_g[i+1], height[i])
        
        
        res = 0
        for i in range(n):
            t = min(next_g[i], prev_g[i]) - height[i]
            res += t if t > 0 else 0
        return res

            

# def trap_rain_water(height):
#     if not height or len(height) < 3:
#         return 0
    
#     stack = []
#     total_water = 0
    
#     for i in range(len(height)):
#         while stack and height[stack[-1]] < height[i]:
#             bottom_idx = stack.pop()
#             bottom_height = height[bottom_idx]
            
#             if not stack:
#                 break
            
#             left_wall_idx = stack[-1]
#             right_wall_idx = i
            
#             left_wall_height = height[left_wall_idx]
#             right_wall_height = height[right_wall_idx]
            
#             width = right_wall_idx - left_wall_idx - 1
#             bounded_height = min(left_wall_height, right_wall_height) - bottom_height
            
#             total_water += width * max(0, bounded_height)
        
#         stack.append(i)
    
#     return total_water
