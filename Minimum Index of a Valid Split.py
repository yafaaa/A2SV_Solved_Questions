class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums)
        f = next(([k,v] for k, v in d.items() if v>n//2), None)
        if not f:
            return -1
        dom_k, dom_f = f
        fre_l, fre_r = 0, dom_f
        for i in range(n):
            if nums[i] == dom_k:
                fre_l += 1
                fre_r -= 1
            len_r = n-1 - i
            len_l = i+1
            if fre_r>len_r//2 and fre_l>len_l//2:
                return i
        return -1
            
