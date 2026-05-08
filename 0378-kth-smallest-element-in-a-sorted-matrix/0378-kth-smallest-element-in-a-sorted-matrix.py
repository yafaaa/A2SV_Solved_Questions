class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        min_heap = []

        for r in range(min(n,m)):
            min_heap.append((matrix[r][0], r , 0))
        heapq.heapify(min_heap)
        ans = 0
        for _ in range(k):
            ans, r, c = heapq.heappop(min_heap)

            if c+1 < m:
                heapq.heappush(min_heap,(matrix[r][c+1], r, c+1))
        return ans



            
        