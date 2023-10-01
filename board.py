from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.__create_debug_board()
        # print("Insert board line by line")
        # for i in range (0, board_size):
        #   line = input().split()
        #   for j in range (0, board_size):
        #     p = Piece(line[j], 1)
        #     board[i].append(p)

        self.print_board()

    def get_piece_at_row_col(self, row, col):
        return self.board[row][col]

    def for_each_piece(self, func):
        for row_index, row in enumerate(self.board):
            for piece_index, piece in enumerate(row):
                func(piece, row_index, piece_index)

    def print_board(self):
        for row in self.board:
            for piece in row:
                print(piece.letter, end="")
            print()
        print()

    def set_piece_at_row_col(self, row, col, item):
        self.board[row][col] = item

    def __create_debug_board(self):
        for i in range(0, 4):
            self.board.append([])

        self.board[0].append(Piece("h"))
        self.board[0].append(Piece("e"))
        self.board[0].append(Piece("l"))
        self.board[0].append(Piece("l"))

        self.board[1].append(Piece("a"))
        self.board[1].append(Piece("b"))
        self.board[1].append(Piece("c"))
        self.board[1].append(Piece("o"))

        self.board[2].append(Piece("d"))
        self.board[2].append(Piece("e"))
        self.board[2].append(Piece("f"))
        self.board[2].append(Piece("g"))

        self.board[3].append(Piece("h"))
        self.board[3].append(Piece("i"))
        self.board[3].append(Piece("j"))
        self.board[3].append(Piece("k"))
