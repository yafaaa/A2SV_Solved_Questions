class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lgth = 0
        for strs in wordDict:
            cnt = s.count(strs)
            if cnt == 0:
                return False
            lgth += len(strs) * cnt
        return len(s) == lgth
            
        
