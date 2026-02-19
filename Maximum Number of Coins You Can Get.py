class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort(reverse=True)
        c = 1
        res = 0
        for i in range(n):
            res += piles[c]
            c += 2
        return res

