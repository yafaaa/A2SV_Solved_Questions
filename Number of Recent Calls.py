from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.a = 0
        self.cnt = 0
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.cnt += 1
        self.a = t-3000
        while self.requests and self.requests[0]<self.a:
            self.requests.popleft()
            self.cnt -= 1
        return self.cnt


        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
