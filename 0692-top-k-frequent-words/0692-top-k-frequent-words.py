class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        min_heap = [(v,k) for k, v in d.items()]
        s = sorted(d.items(), key = lambda x: (-x[1], x[0]))
        ans = []
        for i in range(k):
            ans.append(s[i][0])
        return ans
        



