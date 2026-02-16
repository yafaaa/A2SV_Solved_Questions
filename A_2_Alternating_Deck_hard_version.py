
for  _ in range(int(input())):
    n = int(input())
    cnt = 5
    aw, ab, bw, bb= 1, 0, 0, 0
    n -= 1
    while n > 0:

        m = min(cnt, n)
        mid = m//2
        if m%2 == 0:
            bw += mid
            bb += mid
        else:
            bb += mid + 1
            bw += mid
        cnt += 4
        n -= m
        if n == 0:
            break

        m = min(cnt, n)
        mid = m//2
        if m%2 == 0:
            aw += mid
            ab += mid
        else:
            aw += mid + 1
            ab += mid 
            
        cnt += 4
        n -= m
        if n == 0:
            break
        
    print(f"{aw} {ab} {bw} {bb}")


    







    
 
# for _ in range(int(input())):
#     n = int(input())
    
#     aw, ab, bw, bb = 1, 0, 0, 0
#     n -= 1
#     total = 1 
#     cnt = 2
    
#     while n > 0:
        
#         m = min(cnt, n)
#         w, b = m // 2, m // 2
#         if m % 2 == 1:
#             if (total + 1) % 2 != 0:
#                 w += 1 
#             else: 
#                 b += 1   

#         bw += w
#         bb += b
#         total += m
#         n -= m
#         cnt += 1
#         if n == 0: 
#             break

        
#         m = min(cnt, n)
#         w, b = m // 2, m // 2
#         if m % 2 == 1:
#             if (total + 1) % 2 != 0: 
#                 w += 1
#             else: 
#                 b += 1

#         bw += w
#         bb += b
#         total += m
#         n -= m
#         cnt += 1
#         if n == 0: 
#             break

        
#         m = min(cnt, n)
#         w, b = m // 2, m // 2
#         if m % 2 == 1:
#             if (total + 1) % 2 != 0: 
#                 w += 1
#             else: 
#                 b += 1
#         aw += w 
#         ab += b 
#         total += m
#         n -= m
#         cnt += 1
#         if n == 0: 
#             break

        
#         m = min(cnt, n)
#         w, b = m // 2, m // 2
#         if m % 2 == 1:
#             if (total + 1) % 2 != 0: w += 1
#             else: b += 1
#         aw += w
#         ab += b 
#         total += m
#         n -= m
#         cnt += 1
#         if n == 0:
#             break
        
#     print(f"{aw} {ab} {bw} {bb}")









