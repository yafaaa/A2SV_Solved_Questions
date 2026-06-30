class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @cache        
        def dp(i):
            if i == 0:
                return [1]
            if i == 1:
                return [1, 1]
            lst = [1]
            prev = dp(i-1)
            for j in range(len(prev)-1):
                lst.append(prev[j] + prev[j+1])
            return lst + [1]
        return dp(rowIndex)

        