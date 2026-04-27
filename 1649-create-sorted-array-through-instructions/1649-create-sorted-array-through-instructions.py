class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n  = len(instructions)
        less = [0] * n
        greater = [0] * n
        mod = 10 ** 9 + 7

        def merge(l,r):
            if l == r:
                return [[instructions[l], l]]

            mid = (l+r)//2

            left_arr = merge(l,mid)
            right_arr = merge(mid+1, r)

            
            for num, idx in right_arr:
                less[idx] += bisect_left(left_arr, [num, -inf]) 
                greater[idx] += len(left_arr) - bisect_right(left_arr, [num, inf]) 

            
            return sorted(left_arr + right_arr)

        merge(0, n-1)
        return sum(min(less[i],greater[i])%mod for i in range(n))%mod