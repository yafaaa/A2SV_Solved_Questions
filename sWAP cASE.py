def swap_case(s):
    l = []
    for a in s:
        if a.islower():
            l.append(a.upper())
        else:
            l.append(a.lower())
    return "".join(l)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
