class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        i = 0
        while i <= n:
            b = n - i

            if i > b:
                break

            s[i], s[b] = s[b], s[i]
            i += 1
