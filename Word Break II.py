class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        wordDict = set(wordDict)
        def fun(arr, string):

            if not string:
                ans.append(" ".join(arr))
                return
            curr_string = ""
            for i in range(len(string)):
                ch = string[i]
                curr_string += ch
                if curr_string in wordDict:
                    arr.append(curr_string)
                    fun(arr, string[i+1:])
                    arr.pop()
        fun([],s)
        return ans
