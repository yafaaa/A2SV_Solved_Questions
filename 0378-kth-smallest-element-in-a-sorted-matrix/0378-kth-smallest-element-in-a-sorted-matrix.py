class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        lst = []
        for i in range(n):
            lst.extend(matrix[i])
        heapq.heapify(lst)
        ans = 0
        for _ in range(k):
            ans = heapq.heappop(lst)
        return ans
        