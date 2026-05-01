n, k = map(int, input().split())
scores = list(map(int, input().split()))
 
kth_score = scores[k - 1]
advancers = 0
 
for score in scores:
    if score >= kth_score and score > 0:
        advancers += 1
    else:
        break
 
print(advancers)