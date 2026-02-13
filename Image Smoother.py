class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        y, x = len(img), len(img[0])
        res = [[0]*x for _ in range(y)]

        for r in range(y):
            for c in range(x):
                up = max(0, r-1)
                down = min(y-1, r+1)
                left = max(0, c-1)
                right = min(x-1, c+1)
                
                summ = 0
                for i in range(up, down+1):
                    for j in range(left, right+1):
                        summ += img[i][j]

                len_y = (down - up) + 1
                len_x = (right - left) + 1

                res[r][c] = summ//(len_y*len_x)

        return res
