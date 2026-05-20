class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap=[]
        heapq.heapify(max_heap)
        for i in range(len(capital)):
            capital[i] = (capital[i], i)
        capital.sort(key=lambda x: x[0])
        
        i = 0

        for _ in range(k):

            while i < len(capital) and capital[i][0] <= w:
                idx = capital[i][1]
                heapq.heappush(max_heap, -profits[idx])
                i += 1
            
            if not max_heap:
                return w

            print(max_heap[0])
            w += -heapq.heappop(max_heap)
            
        return w
            
