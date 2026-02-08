from collections import deque
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        d_top = dict()
        for domain in cpdomains:
            rep, d = domain.split()
            dq = deque(d.split("."))
            rep = int(rep)
    
            while dq:
                curr = ".".join(dq)
                d_top[curr] = d_top.get(curr, 0) + rep
                dq.popleft()

                
        return [f"{rep} {domain}" for domain, rep in d_top.items()]

