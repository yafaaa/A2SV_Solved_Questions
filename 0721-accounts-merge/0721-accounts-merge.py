class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                return x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                parent[rooty] = rootx
        
        email_to_idx = {}

        for i, lst in enumerate(accounts):
            for email in lst[1:]:
                if email in email_to_idx:
                    union(i, email_to_idx[email])
                else:
                    email_to_idx[email] = i

        acc = defaultdict(list)

        for email, idx in email_to_idx.items():
            acc[find(idx)].append(email)
        
        ans = []

        for idx, emails in acc.items():
            name = accounts[idx][0]
            ans.append( [name] + sorted(emails))
        
        return ans

