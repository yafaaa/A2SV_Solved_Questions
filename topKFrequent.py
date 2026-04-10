class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        n = max(d.values())+1
        bucket = [[] for _ in range (n)]

        for key ,cnt in d.items():
            bucket[cnt].append(key)
        ans = []
        for i in range(n-1, -1, -1):
            if not k:
                break
            if bucket[i]:
                ans.extend(bucket[i])
                k -= len(bucket[i])
        return ans
            


        


