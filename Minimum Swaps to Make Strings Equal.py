class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt_xy, cnt_yx = 0, 0
        t = 0
        n = len(s1)
        d = Counter(s1)
        d.update(s2)
        if any(v%2 != 0 for k, v in d.items()):
            return -1

        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    cnt_xy += 1
                else:
                    cnt_yx += 1
        
        return (cnt_xy//2) + (cnt_yx//2) + (cnt_yx % 2) + (cnt_xy  % 2)
      
