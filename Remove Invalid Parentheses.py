class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(ch)
        opn_cnt = stack.count("(")
        clse_cnt = stack.count(")")

        ans = []
        seen = set()

        def fun(arr, i, ro, rc, b):
            if b<0:
                return 
            if i == len(s):
                if b == 0:
                    curr_s = "".join(arr[:])
                    if curr_s not in seen:
                        ans.append(curr_s)
                        seen.add(curr_s)
                return
            if s[i] == "(" and ro < opn_cnt:
                fun(arr, i+1, ro+1, rc, b)
            if s[i] == ")" and rc < clse_cnt:
                fun(arr, i+1, ro, rc+1, b)
                

            arr.append(s[i])
            
            if s[i] == ")":
                b -= 1
            elif s[i] == "(":
                b += 1

            fun(arr, i+1, ro, rc, b)

            arr.pop()
        
        fun([], 0, 0, 0,0)
        return ans

            







        
