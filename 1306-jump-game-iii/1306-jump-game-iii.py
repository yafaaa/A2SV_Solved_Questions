class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        @cache
        def dp(i):
            if i in visited:
                return False
            if i >= n or i < 0:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            if dp(i+arr[i]):
                return True
            if dp(i-arr[i]):
                return True
            return False
        return dp(start)

