from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        map_to_d = defaultdict(list)

        seen = set()

        for k, v in d.items():
            seen.add(v)
            map_to_d[v].append(k)
        l = sorted(seen, reverse=True)
        res = []
        for val in l:
            for k, in map_to_d[val]:
                v = d[k]
                res.append(k*v)
        return "".join(res)




