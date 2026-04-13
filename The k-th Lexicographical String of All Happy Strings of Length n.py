class Solution:
    def getHappyString(self, n: int, k: int) -> str:
    
        ans = []
        def fun(arr):

            if len(arr) == n:
                ans.append("".join(arr[:]))
                return
            
            for ch in ["a", "b", "c"]:
                if not arr or arr[-1] != ch:
                    arr.append(ch)
                    fun(arr)
                    arr.pop()
        fun([])
        return ans[k-1] if k <= len(ans) else ""
