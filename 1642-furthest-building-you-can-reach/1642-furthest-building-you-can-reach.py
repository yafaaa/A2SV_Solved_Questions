class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev = heights[0]
        min_heap = []
        heapq.heapify(min_heap)
        build = 0
        for i in range(1, len(heights)):
            diff = heights[i] - prev
            if diff > 0:
                if ladders:
                    heapq.heappush(min_heap, diff)
                    ladders -= 1
                else :
                    t = heapq.heappushpop(min_heap, diff)
                    if t <= bricks:
                        bricks -= t
                    else:
                        return build
            build += 1
            prev = heights[i]
        return build

