def solve():
    word = input()
 
    if not word:
        print("")
        return
 
    result = word[0].upper() + word[1:]
    print(result)
 
if __name__ == '__main__':
    solve()