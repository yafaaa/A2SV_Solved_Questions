def abbreviate_word(word):
    if len(word) > 10:
        abbreviation = f"{word[0]}{len(word) - 2}{word[-1]}"
        return abbreviation
    else:
        return word
 
def main():
    n = int(input(""))
 
    words = [input().strip() for _ in range(n)]
 
    abbreviated_words = [abbreviate_word(word) for word in words]
 
    for word in abbreviated_words:
        print(word)
 
if __name__ == "__main__":
    main()