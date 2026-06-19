class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]
        max_side = 0

        def solve(i, j):
            nonlocal max_side
            if i >= m or j >= n:
                return 0
                
            if matrix[i][j] == '0':
                return 0
                
            if memo[i][j] != -1:
                return memo[i][j]
            
            right = solve(i, j + 1)
            down = solve(i + 1, j)
            diagonal = solve(i + 1, j + 1)
            
            memo[i][j] = 1 + min(right, down, diagonal)
            
            max_side = max(max_side, memo[i][j])
            
            return memo[i][j]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    solve(r, c)
                    
        return max_side * max_side