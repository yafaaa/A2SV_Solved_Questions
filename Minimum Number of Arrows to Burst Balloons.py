class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = []
        x,y = points[0]
        cnt = 0
        for i in range(1,len(points)):

            if  points[i][0] > y:
                cnt += 1
                y = points[i][1]
            else:
                x = max(x, points[i][0])
                y = min(y, points[i][1])
        return cnt+1
            
        
        
        return cnt+1

            

    
