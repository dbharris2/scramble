class EnglishDictionary:
    def __init__(self):
        self.words = set()
        f = open("dictionary.txt", "r")
        for line in f.readlines():
            self.words.add(line.rstrip())

    def get_words(self):
        return self.words
