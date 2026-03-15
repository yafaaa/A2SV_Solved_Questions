class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                p = stack.pop()
                stack[-1] += 1 if not p else p*2
        
        return stack[0]
