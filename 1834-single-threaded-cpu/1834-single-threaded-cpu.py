class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        
        min_heap = []
        heapq.heapify(min_heap)

        b = 0
        curr_time = 0
        ans = []

        while len(ans) != len(tasks):

            while b < len(tasks):
                if tasks[b][0] <= curr_time:
                    heapq.heappush(min_heap, (tasks[b][1], tasks[b][2],tasks[b][0]))
                    b += 1
                else:
                    break
                
            
            if min_heap:
                pt, idx, e = heapq.heappop(min_heap)
                curr_time += pt
                ans.append(idx)

            elif b < len(tasks):
                e, pt, idx = tasks[b]
                curr_time = e    
            

        return ans
        

        
            




            