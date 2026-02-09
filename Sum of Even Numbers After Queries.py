class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        summ = sum(n for n in nums if n%2==0)
        for q in queries:
            val, idx = q
            new_val = nums[idx] + val
            if nums[idx]%2 == 0:
                if new_val % 2 == 0:
                    summ += (new_val - nums[idx])
                else:
                    summ -= nums[idx]
            elif new_val%2 == 0:
                summ += new_val
            nums[idx] = new_val
            res.append(summ)
        return res
