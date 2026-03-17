class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack=[]
        arr=[0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                p=stack.pop()
                arr[p]=i-p
            stack.append(i)
        return arr

        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # num = len(temperatures)
        # arr = [0] * num
        # for i in range(num):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         t = stack.pop()
        #         arr[t] = i-t
        #     stack.append(i)
        # return arr
        
