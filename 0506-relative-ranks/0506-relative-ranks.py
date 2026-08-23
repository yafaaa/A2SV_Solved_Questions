class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss = sorted(score, reverse=True)
        d = dict()
        for i, num in enumerate(ss):
            if i == 0:
                d[num] = "Gold Medal"
            elif i == 1:
                d[num] = "Silver Medal"
            elif i == 2:
                d[num] = "Bronze Medal"
            else:
                d[num] = str(i+1)
        
        for i, num in enumerate(score):
            score[i] = d[score[i]]
            
        return score
            

            