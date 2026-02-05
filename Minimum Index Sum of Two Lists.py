class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict()
        res = []
        min = 2001
        for i , a in enumerate(list1):
            if a in d:
                continue
            d[a]=i
        for i, a in enumerate(list2):
            if a in d:
                if d[a]+i<min:
                    print("fuck")
                    res = []
                    res.append(a)
                    min = d[a]+i
                elif d[a]+i==min:
                    res.append(a)
        return res
                    

