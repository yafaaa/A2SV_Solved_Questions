s1 = input()
s2 = input()
 
s1_lower = s1.lower()
s2_lower = s2.lower()
 
if s1_lower < s2_lower:
    print("-1")
elif s1_lower > s2_lower:
    print("1")
else:
    print("0")