class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = position[-1] - position[0]
        ans = 1

        def fun(force):
            curr_ball = m - 1
            prev = position[0]

            for p in position[1:]:
                if abs(p-prev)>=force:
                    prev = p
                    curr_ball -= 1
                    if not curr_ball:
                        break
            return not curr_ball
        
        while l <= r:
            mid = (l+r)//2
            
            if fun(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans 
