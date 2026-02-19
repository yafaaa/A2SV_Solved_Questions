class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for num in range(n, 1, -1):
            idx = arr.index(num)

            if num-1 == idx:
                continue
            
            arr[:idx+1] = arr[:idx+1][::-1]

            res.append(idx+1)
            
            idx = num-1 # num-1 where is should be

            arr[:idx+1] = arr[:idx+1][::-1]

            res.append(num)

        return res
