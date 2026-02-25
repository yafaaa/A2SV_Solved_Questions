
def fun():
    string = input()
    n = len(string)
    prev = 1
    res = []
    for i in range(1,n):
        if string[i-1] != string[i]:
            if prev%2 != 0:
                res.append(string[i-1])
            prev = 1
            continue
        prev += 1
    if prev%2 != 0:
        res.append(string[-1])
    return "".join(sorted(set(res)))


if __name__ == "__main__":
    for _ in range(int(input())):
        print(fun())
