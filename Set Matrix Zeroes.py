class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        l = []
        col_set = set()
        row_set = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    col_set.add(c)
                    row_set.add(r)

        for r in range(row):
            if r in row_set:
                matrix[r] = [0] * col
            else:
                for c in col_set:
                    matrix[r][c] = 0
        


