class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        res = []
        
        def add(r,c):
            board[r][c] = 'Q'
            for y in range(n):
                for x in range(n):
                    if y == r or x == c or y-x == r-c or y+x == r+c:
                        if board[y][x] != "Q":
                            board[y][x] += 1
        
        def remv(r,c):
            for y in range(n):
                for x in range(n):
                    if y == r or x == c or y-x == r-c or y+x == r+c:
                        if board[y][x] == "Q":
                            board[y][x] = 0
                        else:
                            board[y][x] -= 1
        
        
        def fun(row, board):
            
            if row == n:
                res.append(deepcopy(board))
                return
            
            for i in range(n):
                if board[row][i] == 0:
                    add(row, i)
                    fun(row+1, board)
                    remv(row, i)
            
        fun(0, board)
        
        return len(res)


            
            

        
        
        
