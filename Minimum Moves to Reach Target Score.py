class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = target
        ans = 0
        while True:
            if curr%2:
                ans += 1
                curr -= 1
            elif maxDoubles and curr>1:
                curr //=2
                maxDoubles -= 1
                ans += 1
            else:
                ans += curr-1
                return ans
