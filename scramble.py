from board import Board
from dictionary import EnglishDictionary

dictionary = EnglishDictionary()
board = Board()
board_size = 4
results = {}

letters = {
    "a": 1,
    "b": 4,
    "c": 4,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 3,
    "h": 3,
    "i": 1,
    "j": 10,
    "k": 5,
    "l": 2,
    "m": 4,
    "n": 2,
    "o": 1,
    "p": 4,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 2,
    "v": 5,
    "w": 2,
    "x": 8,
    "y": 3,
    "z": 1,
}


def find_word(word, word_index, row, col, value):
    curr_letter = word[word_index]
    increase_value = lambda val: val + letters[curr_letter]

    piece = board.get_piece_at_row_col(row, col)

    if piece.visited:
        return
    if word_index == len(word) - 1:
        if not word in results:
            # print("Found word: " + word)
            results[word] = increase_value(value)
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
        == board.get_piece_at_row_col(nextRow, nextCol).letter
    )

    # Up-Left
    if can_go_up and can_go_left and is_next_letter_valid(row - 1, col - 1):
        # print("Up-Left")
        find_word(
            word,
            word_index + 1,
            row - 1,
            col - 1,
            increase_value(value),
        )
    # Up
    if can_go_up and is_next_letter_valid(row - 1, col):
        # print("Up")
        find_word(
            word,
            word_index + 1,
            row - 1,
            col,
            increase_value(value),
        )
    # Up-Right
    if can_go_up and can_go_right and is_next_letter_valid(row - 1, col + 1):
        # print("Up-Right")
        find_word(
            word,
            word_index + 1,
            row - 1,
            col + 1,
            increase_value(value),
        )
    # Right
    if can_go_right and is_next_letter_valid(row, col + 1):
        # print("Right")
        find_word(
            word,
            word_index + 1,
            row,
            col + 1,
            increase_value(value),
        )
    # Right-Down
    if can_go_down and can_go_right and is_next_letter_valid(row + 1, col + 1):
        # print("Right-Down")
        find_word(
            word,
            word_index + 1,
            row + 1,
            col + 1,
            increase_value(value),
        )
    # Down
    if can_go_down and is_next_letter_valid(row + 1, col):
        # print("Down")
        find_word(
            word,
            word_index + 1,
            row + 1,
            col,
            increase_value(value),
        )
    # Down-Left
    if can_go_down and can_go_left and is_next_letter_valid(row + 1, col - 1):
        # print("Down-Left")
        find_word(
            word,
            word_index + 1,
            row + 1,
            col - 1,
            increase_value(value),
        )
    # Left
    if can_go_left and is_next_letter_valid(row, col - 1):
        # print("Left")
        find_word(
            word,
            word_index + 1,
            row,
            col - 1,
            increase_value(value),
        )

    piece.visited = False


def start_find_word(word):
    for row in range(0, board_size):
        for col in range(0, board_size):
            piece = board.get_piece_at_row_col(row, col)
            if piece.letter == word[0]:
                # print("Find word " + word)
                find_word(
                    word,
                    0,
                    row,
                    col,
                    0,
                )


def find_words():
    for word in dictionary.get_words():
        if len(word) <= 1:
            continue
        if len(word) > (board_size * board_size):
            continue
        start_find_word(word)


def print_results():
    for word, value in sorted(results.items(), key=lambda x: x[1]):
        print(word, value)


find_words()
print_results()
