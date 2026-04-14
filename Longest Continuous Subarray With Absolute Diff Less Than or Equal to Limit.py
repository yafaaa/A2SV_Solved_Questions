class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  
        min_deque = deque()  
        a = 0
        max_len = 0

        for b, val in enumerate(nums):
            while max_deque and nums[max_deque[-1]] < val:
                max_deque.pop()
            max_deque.append(b)

            while min_deque and nums[min_deque[-1]] > val:
                min_deque.pop()
            min_deque.append(b)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                a += 1
                if max_deque[0] < a:
                    max_deque.popleft()
                if min_deque[0] < a:
                    min_deque.popleft()

            max_len = max(max_len, b - a + 1)

        return max_len

