class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for a in nums:
            xor = xor ^ a
        return xor
          
