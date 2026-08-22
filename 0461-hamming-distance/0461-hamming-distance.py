class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        while x > 0 or y > 0:
            
            if (x % 2) != (y % 2): #is there bit differnt??
                distance += 1

            x //= 2  #next bit
            y //= 2
        return distance

