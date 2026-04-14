class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        ans = []
        def fun(arr,used):
            if ans:
                return ans
            if len(arr) == len(pattern)+1:
                ans.append(arr[:])
                return

            for i in range(1,10):
                if i not in used:
                    
                    if len(arr)>0:
                        curr_pat = pattern[len(arr)-1]
                        last = int(arr[-1])

                        if curr_pat == "I" and not(last < i):
                            continue
                        if curr_pat == "D" and not (last > i):
                            continue
                    arr.append(i)
                    used.add(i)
                    fun(arr, used)

                    arr.pop()
                    used.remove(i)
            
        fun([],set())
        return "".join(map(str,ans[0]))
