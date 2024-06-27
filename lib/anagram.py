# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []

        for i in word_list:
            if sorted([letter for letter in i]) == sorted([letter for letter in self.word]):
                matches.append(i)
        
        return matches
