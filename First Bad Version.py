# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def fun(l,r):
            while l <= r:
                m = (l+r)//2
                if isBadVersion(m):
                    r = m-1
                else:
                    l = m+1
            return l

        return fun(1,n)
