class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        max_heap = [(-v,k) for k, v in d.items()]
        heapq.heapify(max_heap)
        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        return ans