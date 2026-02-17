class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r, c = rStart , cStart
        res = [[r,c]]
        direction = [[0,1], [1,0], [0,-1], [-1,0]] # r, d, l ,u
        steps = 1
        i = 0
        while len(res) != rows*cols:

            for _ in range(2): # (r & d) and (l & u)
                for _ in range(steps):
                    r += direction[i][0]
                    c += direction[i][1]

                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r,c])
                    
                i = (i + 1) % 4
            steps += 1
        return res
