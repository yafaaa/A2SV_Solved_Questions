class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0]*n for _ in range(n)]
        res = []

        def add(r,c):
            board[r][c] = "Q"
            for x in range(n):
                for y in range(n):
                    if y == r or x == c or r-c == y-x or r+c == y+x:
                        if board[y][x] != 'Q':
                            board[y][x] += 1
                    
                        
            
        def remv(r,c):
            
            for x in range(n):
                for y in range(n):
                    if y == r or x == c or r-c == y-x or r+c == y+x:
                        if board[y][x] == 'Q':
                            board[y][x] = 0
                        else:
                            board[y][x] -= 1


        def backtrack(row, board):
            if row == n:
                res.append(deepcopy(board))
                return 
            for i in range(n):
                if board[row][i] == 0:
                    add(row,i)
                    backtrack(row+1, board)
                    remv(row,i)
        



        backtrack(0, board)
        ans = []
        for brd in res:
            temp2 = []
            for row in brd:
                temp = ""
                for ch in row:
                    if ch != "Q":
                        temp += "."
                    else:
                        temp += "Q"
                temp2.append(temp)
            ans.append(temp2)


        return ans
