class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        n = len(s)

        @cache
        def dp(i):
            if i == n:
                return True
            for j in range(i,n):
                t = s[i: j+1]
                if t in d:
                    if dp(j+1):
                        return True
            return False
        return dp(0)

            

