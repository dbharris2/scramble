from dictionary import EnglishDictionary
from letters import letters

board_size = 4


class WordFinder:
    def __init__(self, board):
        self.board = board
        self.dictionary = EnglishDictionary()
        self.results = {}

    def find_words(self):
        self.results = {}
        for word in self.dictionary.get_words():
            if len(word) <= 1:
                continue
            if len(word) > (board_size * board_size):
                continue
            self.__start_find_word(word)
        return self.results

    def __start_find_word(self, word):
        for row in range(0, board_size):
            for col in range(0, board_size):
                piece = self.board.get_piece_at_row_col(row, col)
                if piece.letter == word[0]:
                    # print("Find word " + word)
                    self.__find_word(
                        word,
                        0,
                        row,
                        col,
                        0,
                    )

    def __find_word(self, word, word_index, row, col, value):
        curr_letter = word[word_index]
        increase_value = lambda val: val + letters[curr_letter]

        piece = self.board.get_piece_at_row_col(row, col)

        if piece.visited:
            return
        if word_index == len(word) - 1:
            if not word in self.results:
                # print("Found word: " + word)
                self.results[word] = increase_value(value)
            return

        curr_letter = word[word_index]
        # print(word, curr_letter)
        piece.visited = True

        can_go_up = row > 0
        can_go_down = row < board_size - 1
        can_go_left = col > 0
        can_go_right = col < board_size - 1

        is_next_letter_valid = (
            lambda nextRow, nextCol: word[word_index + 1]
            == self.board.get_piece_at_row_col(nextRow, nextCol).letter
        )

        # Up-Left
        if can_go_up and can_go_left and is_next_letter_valid(row - 1, col - 1):
            # print("Up-Left")
            self.__find_word(
                word,
                word_index + 1,
                row - 1,
                col - 1,
                increase_value(value),
            )
        # Up
        if can_go_up and is_next_letter_valid(row - 1, col):
            # print("Up")
            self.__find_word(
                word,
                word_index + 1,
                row - 1,
                col,
                increase_value(value),
            )
        # Up-Right
        if can_go_up and can_go_right and is_next_letter_valid(row - 1, col + 1):
            # print("Up-Right")
            self.__find_word(
                word,
                word_index + 1,
                row - 1,
                col + 1,
                increase_value(value),
            )
        # Right
        if can_go_right and is_next_letter_valid(row, col + 1):
            # print("Right")
            self.__find_word(
                word,
                word_index + 1,
                row,
                col + 1,
                increase_value(value),
            )
        # Right-Down
        if can_go_down and can_go_right and is_next_letter_valid(row + 1, col + 1):
            # print("Right-Down")
            self.__find_word(
                word,
                word_index + 1,
                row + 1,
                col + 1,
                increase_value(value),
            )
        # Down
        if can_go_down and is_next_letter_valid(row + 1, col):
            # print("Down")
            self.__find_word(
                word,
                word_index + 1,
                row + 1,
                col,
                increase_value(value),
            )
        # Down-Left
        if can_go_down and can_go_left and is_next_letter_valid(row + 1, col - 1):
            # print("Down-Left")
            self.__find_word(
                word,
                word_index + 1,
                row + 1,
                col - 1,
                increase_value(value),
            )
        # Left
        if can_go_left and is_next_letter_valid(row, col - 1):
            # print("Left")
            self.__find_word(
                word,
                word_index + 1,
                row,
                col - 1,
                increase_value(value),
            )

        piece.visited = False
