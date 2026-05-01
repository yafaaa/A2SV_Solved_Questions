def solve():
    n_str = input()
    
    lucky_digit_count = 0
    for char in n_str:
        if char == '4' or char == '7':
            lucky_digit_count += 1
            
    if lucky_digit_count == 4 or lucky_digit_count == 7:
        print("YES")
    else:
        print("NO")
 
solve()