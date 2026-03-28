# n = int(input())
# nums = list(map(int, input().split()))

# summ = sum(nums)
# def b(nums):
#     res = []

#     def fun(i, curr):
        
#         if i == n:
#             if len(curr) > 0 and len(curr) < n:
#                 res.append(curr[:])
#             return
#         curr.append(nums[i])
#         fun(i+1, curr)
#         curr.pop()

#         fun(i+1, curr)

#     fun(0, [])

#     return len(res)

# print(b(nums))


n = int(input())
nums = list(map(int, input().split()))

summ = sum(nums)
def b(nums):
    mn = float('inf')
    if len(nums) == 1:
        return nums[0]
    def fun(i, curr):
        nonlocal mn
        if i == n:
            if len(curr) > 0 and len(curr) < n:
                s = sum(curr)
                r = summ-s
                a = abs(r-s)
                mn = min(a, mn)
            return
        curr.append(nums[i])
        fun(i+1, curr)
        curr.pop()

        fun(i+1, curr)

    fun(0, [])

    return mn

print(b(nums))









# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort(reverse=True)
# a, b = 0, 0
# for num in nums:
#     if b<a:
#         b += num
#     else:
#         a += num
# print(abs(b-a))