from collections import Counter
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    nums = list(map(int, input().split()))
    m = min(l,r)
    
    left_dict = Counter(nums[:l])
    right_dict = Counter(nums[l:])
    
    for k in nums[l:]:
        if k in left_dict:
            mn_val = min(left_dict[k], right_dict[k])
            left_dict[k] -= mn_val
            right_dict[k] -= mn_val
            l -= mn_val
            if not left_dict[k]:
                del left_dict[k]
                
            if not right_dict[k]:
                del right_dict[k]
            r -= mn_val
    move = 0
    
    if l < r:
        dis, total_val = 0, 0

        for k, v in right_dict.items():
            dis = v%2
            total_val += v-dis
        
        for i in range((r-l)//2):
            if total_val:
                total_val -= 2
                move += 1

            else:
                dis -= 1
                move += 2
        move += l
            
        
    elif r < l:
            dis, total_val = 0, 0

            for k, v in left_dict.items():
                dis = v%2
                total_val += v-dis

            for i in range((l-r)//2):
                if total_val:
                    total_val -= 2
                    move += 1

                else:
                    dis -= 1
                    move += 2
            move += r
                        
    else:
        move += l            
    
    print(move)
