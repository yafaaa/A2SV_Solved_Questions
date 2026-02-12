class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        d = dict()
        for i in range(n):
            for j in range(n):
                d[(j,n-1-i)] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = d[(i,j)]


