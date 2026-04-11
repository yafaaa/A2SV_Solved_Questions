from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        d = defaultdict(list)
        c = 97
        for i in range(2,10):
            if i == 7 or i == 9:
                for j in range(4):
                    d[i].append(chr(c+j))
                c += 4
            else:
                for j in range(3):
                    d[i].append(chr(c+j))
                c += 3

        ans = []
        def fun(arr, i):
            if len(arr) == n:
                ans.append("".join(arr))
                return 
            
            for ch in d[int(digits[i])]:
                arr.append(ch)
                fun(arr, i + 1)
                arr.pop()
        fun([], 0)
        return ans
