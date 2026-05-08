class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        min_heap = []
        for idx_1 in range(min(k, len(nums1))):
            min_heap.append((nums1[idx_1]+nums2[0], idx_1, 0))

        heapq.heapify(min_heap)
        ans = []
        for _ in range(k):
            curr_sum, u, v = heapq.heappop(min_heap)
            ans.append([nums1[u],nums2[v]])
            if v+1 < m:
                heapq.heappush(min_heap, (nums1[u]+nums2[v+1], u, v+1))
        
        return ans
            
            
        