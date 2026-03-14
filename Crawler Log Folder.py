class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for s in logs:
            if s == "../" :
                if c > 0:
                    c-=1
            elif s== "./":
                continue
            else:
                c+=1
        return c
