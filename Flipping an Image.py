class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for l in image:
            l.reverse()
            for i in range(n):
                l[i] = abs(l[i]-1)
        return image
                
