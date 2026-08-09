class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        ans = math.log(n,2)
        return 2 ** int(ans) == n
        
