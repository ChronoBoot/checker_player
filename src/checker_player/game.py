from .board import Board
from .player import Player, HumanPlayer

class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'w'
        self.players = {
            'w': HumanPlayer('w'),
            'b': HumanPlayer('b')
        }

    def is_valid_move(self, start_pos, end_pos):
        piece = self.board.get_piece(*start_pos)
        if piece == ' ' or piece.color != self.current_turn:
            return False

        valid_moves = self.board.get_valid_moves(piece, *start_pos)
        return end_pos in valid_moves

    def make_move(self, start_pos, end_pos):
        if not self.is_valid_move(start_pos, end_pos):
            print("Invalid move")
            return False

        piece = self.board.get_piece(*start_pos)
        valid_moves = self.board.get_valid_moves(piece, *start_pos)
        skipped = valid_moves[end_pos]
        self.board.move_piece(start_pos, end_pos)

        if skipped:
            for skip in skipped:
                self.board.remove_piece(*skip)

        if end_pos[0] == 0 and piece.color == 'w' or end_pos[0] == 7 and piece.color == 'b':
            piece.make_king()

        self.switch_turn()
        return True

    def switch_turn(self):
        self.current_turn = 'b' if self.current_turn == 'w' else 'w'

    def is_game_over(self):
        for color in ['w', 'b']:
            pieces = self.board.get_all_pieces(color)
            if any(self.board.get_valid_moves(piece, row, col) for row, col, piece in pieces):
                return False
        return True

    def play(self):
        while not self.is_game_over():
            self.board.print_board()
            print(f"{self.current_turn}'s turn")
            start_pos = self.players[self.current_turn].get_move()
            end_pos = self.players[self.current_turn].get_move()
            if not self.make_move(start_pos, end_pos):
                print("Invalid move, try again.")

        print("Game over!")

