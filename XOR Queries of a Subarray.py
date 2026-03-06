class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n)
        prefix[0] = arr[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] ^ arr[i]
        res = []
        for a, b in queries:
            ans = prefix[b]
            ans ^= prefix[a-1] if a-1>-1 else 0
            res.append(ans)
        return res
        
