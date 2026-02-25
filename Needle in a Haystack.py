from collections import Counter
def fun():
    needle = input()
    haystack = input()
    d = Counter(haystack)
    
    for ch in needle:
        if ch not in d:
            return "Impossible"
        d[ch] -= 1
        if d[ch] == 0:
            del d[ch]
    haystack = [ k for k, v in d.items() for _ in range(v)]
    haystack.sort()
    n = len(needle)
    m = len(haystack)
    a,b = 0, 0
    res = []
    while a<n and b<m:

        if needle[a] > haystack[b]:
            res.append(haystack[b])
            b += 1
        else:
            res.append(needle[a])
            a += 1
    if a<n:
        res.extend(needle[a:])
    if b<m:
        res.extend(haystack[b:])
    
    return "".join(res)

    

if __name__ == "__main__":
    for _ in range(int(input())):
        print(fun())
