import pygame
from .game import CheckersGame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Set the dimensions of each square on the board
SQUARE_SIZE = 80

# Set the dimensions of the board
BOARD_SIZE = SQUARE_SIZE * 8

class TextUI:
    def __init__(self, game):
        self.game = game

    def get_move_input(self):
        start_pos = input("Enter the start position (row,col): ")
        end_pos = input("Enter the end position (row,col): ")
        start_pos = tuple(map(int, start_pos.split(',')))
        end_pos = tuple(map(int, end_pos.split(',')))
        return start_pos, end_pos

    def play(self):
        while not self.game.is_game_over():
            self.game.board.print_board()
            start_pos, end_pos = self.get_move_input()
            self.game.make_move(start_pos, end_pos)

class PygameUI:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        pygame.display.set_caption('Checkers')
        self.clock = pygame.time.Clock()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else GRAY
                pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.game.board.get_piece(row, col)
                if piece != ' ':
                    piece_color = WHITE if piece.color == 'w' else BLACK
                    pygame.draw.circle(self.screen, piece_color,
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                       SQUARE_SIZE // 2 - 10)
                    if piece.king:
                        pygame.draw.circle(self.screen, BLUE,
                                           (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                           SQUARE_SIZE // 2 - 20)

    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return y // SQUARE_SIZE, x // SQUARE_SIZE

    def play(self):
        running = True
        selected_piece = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.get_mouse_pos()
                    if selected_piece:
                        end_pos = (row, col)
                        start_pos = selected_piece
                        if self.game.make_move(start_pos, end_pos):
                            selected_piece = None
                        else:
                            selected_piece = (row, col)
                    else:
                        selected_piece = (row, col)

            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
