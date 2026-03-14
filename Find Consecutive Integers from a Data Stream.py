from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.lgth = 0
        self.cnt = 0
        self.deque = deque()

    def consec(self, num: int) -> bool:
        self.deque.append(num)
        self.cnt += 1 if num == self.value else 0
        self.lgth += 1
        if self.lgth > self.k:
            self.cnt -= 1 if self.deque[0] == self.value else 0
            self.deque.popleft()
        if self.cnt == self.k:
            return True
        return False

            

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
