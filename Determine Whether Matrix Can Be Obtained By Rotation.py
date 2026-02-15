class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if target == mat:
                return True
        for i in range(3):
            new_mat = [[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    new_mat[c][abs(n-1-r)] = mat[r][c]
            if target == new_mat:
                return True
            mat = new_mat
            
        return False
