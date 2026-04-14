class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <3:
            return False

        def fun(num1,num2,num):
            num3 = num1 + num2

            if num and str(num) == str(num3):
                return True
            t = ""
            for i, ch in enumerate(num):
                t += ch
                if int(t)>0 and t[0] == '0':
                        return 
                if num1 < 0 or num2< 0:
                    if fun(num2, int(t), num[i+1:]):
                        return True
                    continue

                if int(t) == num3:
                   
                    if fun(num2,num3,num[i+1:]):
                        return True

                elif int(t)> num3:
                    return

        return True if fun(-1,-1,num) else False

            
