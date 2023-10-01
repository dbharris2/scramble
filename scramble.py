from board import Board
from wordfinder import WordFinder

board = Board()
word_finder = WordFinder(board)
results = word_finder.find_words()
for word, value in sorted(results.items(), key=lambda x: x[1]):
    print(word, value)
