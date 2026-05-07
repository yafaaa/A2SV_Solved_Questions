class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mx_heap = [-n for n in nums]
        heapq.heapify(mx_heap)
        ans = 0
        for _ in range(k):
            ans = -heapq.heappop(mx_heap)
        return ans





