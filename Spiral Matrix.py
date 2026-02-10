class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        y = len(matrix)
        x = len(matrix[0])
        seen = set()
        res = []
        row, col = 0, -1 
        while len(seen) != x*y:
            
            while col+1 != x:
                col += 1
                if (row,col) in seen:
                    col -= 1
                    break
                seen.add((row,col))
                res.append(matrix[row] [col])
            
            
            while row+1 != y:
                row += 1
                if (row,col) in seen:
                    row -= 1
                    break
                seen.add((row,col))
                res.append(matrix[row] [col])
                

            
            while col-1 != -1:
                col -= 1
                if (row,col) in seen:
                    col += 1
                    break
                seen.add((row,col))
                res.append(matrix[row] [col])
                
            
            
            while row-1 != -1:
                row -= 1
                if (row, col) in seen:
                    row += 1
                    break
                seen.add((row, col))
                res.append(matrix[row] [col])
                
        return res

        
        
