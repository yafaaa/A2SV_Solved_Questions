class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = []
        n = len(s)
        arr =  [0] * n 
        
        for a, b ,c in shifts:
            x = -1 if not c else 1
            arr[a] += x
            if b+1 < n:
                arr[b+1] -= x

        res.append( chr (( (ord(s[0])-ord('a')+arr[0]) % 26) + ord('a')) )

        for i in range(1,n):
            arr[i] = arr[i-1] + arr[i]
            res.append( chr (( (ord(s[i])-ord('a')+arr[i]) % 26) + ord('a')) )
            
        return "".join(res)
