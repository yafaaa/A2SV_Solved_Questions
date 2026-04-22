import copy
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(board), len(board[0])

        def outbound(r,c):
            return r < 0 or r >= n or c < 0 or c >= m
        
        def dfs(r,c, visited):
            
            for dr, dc in direction:
                nw_r = r + dr
                nw_c = c + dc
                
                if outbound(nw_r, nw_c):
                    return True

                if board[nw_r][nw_c] == "O" and (nw_r, nw_c) not in visited:
                    visited.add((nw_r, nw_c))
                    if dfs(nw_r, nw_c, visited):
                        return True

        visited = set()
        for r in range(n):
            for c in range(m):
                if (r,c) not in visited and board[r][c] == "O":
                    t = visited.copy()
                    visited.add((r,c))
                    if dfs(r,c,visited):
                        
                        visited = t
                        
        
        for r, c in visited:
            board[r][c] = "X"
        
        return board


        
                    
                    


            

            