class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict_s = Counter(s)
        res = []
        for ch in order:
            res.append(ch*dict_s[ch]) 
            del dict_s[ch]

        for k, v in dict_s.items():
            res.append(k*v) 
        return "".join(res)
