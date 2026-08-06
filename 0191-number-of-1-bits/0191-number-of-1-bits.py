class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            r = int(math.log(n, 2))
            n -= 2 ** r
            cnt += 1
        return cnt