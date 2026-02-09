class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3 != 0:
            return []
        start = (num//3)-1
        return [start+i for i in range(3)]
            

        
