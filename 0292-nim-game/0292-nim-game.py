class Solution:
    def canWinNim(self, n: int) -> bool:
        
        if n < 4:
            return True
        if not n % 4:
            return False
        return True 