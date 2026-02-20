class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        h_index = 0
        for i in range(n):
            rank = i + 1
            if citations[i] >= rank:
                h_index = rank
            else:
                break
        return h_index













        
       
