# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def fun(l, r):
            mid = (l + r) // 2
            res = guess(mid)
            if not res:
                return mid
            
            elif res == -1:
                return fun(l, mid-1)
            
            else:
                return fun(mid+1, r)

        return fun(1, n)
            