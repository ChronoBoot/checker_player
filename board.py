from piece import Piece
from square import Square


class Board():

    def set_board(self, size):
        self.squares = [[Square(i, j, "white" if (i + j) % 2 == 0 else "black", None) for j in range(size)] for i in range(size)]

    def set_pieces(self, size, player_1_color, player_2_color):
        for i in range(size):
            for j in range(size):
                if (i + j) % 2 == 0:
                    if i < 3:
                        self.squares[i][j].piece = Piece(player_1_color, (i, j))
                    elif i > size - 4:
                        self.squares[i][j].piece = Piece(player_2_color, (i, j))

    def __init__(self, size, player_1_color, player_2_color):
        self.size = size
        self.set_board(size)
        self.set_pieces(size, player_1_color, player_2_color)

    def move_piece(self, piece, old_position, new_position):
        self.squares[old_position[0]][old_position[1]].piece = None
        self.squares[new_position[0]][new_position[1]].piece = piece
        piece.move(new_position)

    