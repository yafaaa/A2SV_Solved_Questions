class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_p = [nums[0]]
        for i in range(1,n):
            forward_p.append(forward_p[i-1]*nums[i])

        product = 1
        back_p = []

        for i in range(n-1, -1, -1):
            product *= nums[i]
            back_p.append(product)

        back_p = back_p[::-1]

        for i in range(n):
            a = 1 if i-1 < 0 else forward_p[i-1]
            b = 1 if i+1 >=n else back_p[i+1]
            nums[i] = a*b
        return nums



            
        

            

