class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def fun(idx):
            return matrix[idx][0] <= target

        l, r = 0, len(matrix)-1
        idx = l
        while l <= r:
            mid = (l+r)//2

            if fun(mid):
                idx = mid
                l = mid + 1
            else:
                r = mid - 1

        row = matrix[idx]

        l, r = 0, len(row) - 1
        
        while l <= r:
            mid = (l+r)//2

            if row[mid] == target:
                return True

            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False



