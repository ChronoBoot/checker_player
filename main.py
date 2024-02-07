from tkinter import *
from enum import Enum

from board import Board

NB_SQUARES_SIDE = 8
WHITE = "white"
BLACK = "black"
BLUE = "blue"
RED = "red"
PIECE_TO_SQUARE_MARGIN = 5

PLAYER_1_COLOR = RED
PLAYER_2_COLOR = BLUE


Direction = Enum('Direction', ['UP_LEFT', 'UP_RIGHT', 'DOWN_LEFT', 'DOWN_RIGHT'])

board_back = Board(NB_SQUARES_SIDE, PLAYER_1_COLOR, PLAYER_2_COLOR)
board = [[None for _ in range(board_back.size)] for _ in range(board_back.size)]

count_square_click = 0
first_pos = None
second_pos = None

def move_piece(old_pos, new_pos):
    print("Moving piece")

    piece = board_back.squares[old_pos[0]][old_pos[1]].piece

    board_back.move_piece(piece, old_pos, new_pos)
    board[old_pos[0]][old_pos[1]].delete("all")
    board[new_pos[0]][new_pos[1]].create_oval(PIECE_TO_SQUARE_MARGIN, PIECE_TO_SQUARE_MARGIN, square_size - PIECE_TO_SQUARE_MARGIN, square_size - PIECE_TO_SQUARE_MARGIN, fill=piece.color)

    print("Piece moved")

def on_square_click(event):
    print("Square clicked")

    widget = event.widget

    print(f"Square clicked: {widget.grid_info()}")

    global count_square_click, first_pos, second_pos
    count_square_click += 1


    if count_square_click == 1:
        first_pos = widget.grid_info().get("row"), widget.grid_info().get("column")

    if count_square_click == 2:
        second_pos = widget.grid_info().get("row"), widget.grid_info().get("column")
        move_piece(first_pos, second_pos)

        count_square_click = 0
    
    print("End square clicked")

def create_board(frame, square_size):
    print("Creating board")

    global board

    for i in range(NB_SQUARES_SIDE):
        for j in range(NB_SQUARES_SIDE):
            bg = board_back.squares[i][j].color

            square = Canvas(frame, bg=bg, width=square_size, height=square_size)
            square.grid(row=i, column=j)
            square.bind("<Button-1>", on_square_click)
            board[i][j] = square

    print("Board created")

    return board

def set_pieces(board, square_size):
    print("Setting pieces")

    for i in range(NB_SQUARES_SIDE):
        for j in range(NB_SQUARES_SIDE):
            piece = board_back.squares[i][j].piece

            if piece:
                board[i][j].create_oval(PIECE_TO_SQUARE_MARGIN, PIECE_TO_SQUARE_MARGIN, square_size - PIECE_TO_SQUARE_MARGIN, square_size - PIECE_TO_SQUARE_MARGIN, fill=piece.color)

    print("Pieces set")

    return board

def get_player(square):
    print("Getting player")

    pos = square.grid_info().get("row"), square.grid_info().get("column")
    
    piece = board_back.squares[pos[0]][pos[1]].piece

    if piece:
        if(piece.color == PLAYER_1_COLOR):
            print("Player 1")
            return 1
        elif(piece.color == PLAYER_2_COLOR):
            print("Player 2")
            return 2
    
    print("No player")
    return 0

def init():
    print("Initializing game")

    root = Tk()
    root.title("Checkers")

    # Get the current screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    screen_size = min(screen_width, screen_height)

    root.geometry(f"{screen_size}x{screen_size}")

    frame = Frame(root)

    global square_size
    square_size = screen_size // NB_SQUARES_SIDE - 10

    board = create_board(frame, square_size)
    set_pieces(board, square_size)
    

    frame.pack()

    print("Game initialized")

    return root

def main():
    print("Starting game")

    root = init()
    root.mainloop()

    print("Game ended")

if __name__ == "__main__":
    main()
