class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        y, x = len(mat), len(mat[0])
        r, c = 0, 0
        res = []
        t = 0
        while t != y*x:

            # upward mover
            while r>-1 and c < x:
                res.append(mat[r][c])
                t+=1
                r -= 1
                c += 1
            
            if c == x: # if left bound was reached
                c -= 1
                r += 2
            else:       # if upper bound was reached
                r += 1
            
            # downward mover
            while r<y and c>-1:
                res.append(mat[r][c])
                t+=1
                r += 1
                c -= 1
            
            if r == y: # if bottom bound was reached
                r -= 1
                c += 2

            else:
                c += 1
            
        return res
            



            

                
