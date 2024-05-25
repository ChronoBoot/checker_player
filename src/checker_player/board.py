from .piece import Piece


class Board:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range((row % 2) - 1, 8, 2):
                board[row][col] = Piece('b')  # black pieces
            for col in range((row % 2), 8, 2):
                board[row + 5][col] = Piece('w')  # white pieces
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(str(piece) if piece != ' ' else '.' for piece in row))

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

    def move_piece(self, start_pos, end_pos):
        piece = self.get_piece(*start_pos)
        self.set_piece(*start_pos, ' ')
        self.set_piece(*end_pos, piece)

    def remove_piece(self, row, col):
        self.board[row][col] = ' '

    def is_within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_all_pieces(self, color):
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece != ' ' and piece.color == color:
                    pieces.append((row, col, piece))
        return pieces

    def get_valid_moves(self, piece, row, col):
        moves = {}
        if piece.color == 'w' or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, col - 1))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, col + 1))
        if piece.color == 'b' or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, 8), 1, piece.color, col - 1))
            moves.update(self._traverse_right(row + 1, min(row + 3, 8), 1, piece.color, col + 1))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == ' ':
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, 8)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= 8:
                break

            current = self.board[r][right]
            if current == ' ':
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, 8)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
