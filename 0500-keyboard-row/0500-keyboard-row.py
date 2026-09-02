class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        thrid_row = "zxcvbnm"

        d = dict()

        for ch in first_row:
            d[ch] = first_row
        
        for ch in second_row:
            d[ch] = second_row
        
        for ch in thrid_row:
            d[ch] = thrid_row

        res = []

        for word in words:
            set_row = set(d[word[0].lower()])
            set_word = set(word.lower())
            if set_word == set_row.intersection(set_word):
                res.append(word)

        return res

        
        