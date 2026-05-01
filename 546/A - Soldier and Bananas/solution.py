k, n, w = map(int, input().split())
 
total_cost = k * (w * (w + 1) // 2)
 
borrow_amount = total_cost - n
 
if borrow_amount <= 0:
    print(0)
else:
    print(borrow_amount)