class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n-1
        s = 0
        for r in range(n-1, -1, -1):
            s += 1
            if people[l] + people[r] <= limit:
                l += 1
            if l >= r:
                break
        return s
            
            
            
