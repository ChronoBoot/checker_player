import pygame
from enum import Enum

NB_SQUARES_SIDE = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PIECE_TO_SQUARE_MARGIN = 5

PLAYER_1_COLOR = RED
PLAYER_2_COLOR = BLUE


Direction = Enum('Direction', ['UP_LEFT', 'UP_RIGHT', 'DOWN_LEFT', 'DOWN_RIGHT'])

pygame.init()

# Get the current screen size
infoObject = pygame.display.Info()
screen_width = infoObject.current_w - 100
screen_height = infoObject.current_h - 100

# Set the screen size to have a square aspect ratio
min_screen_size = min(screen_width, screen_height)
screen_width = min_screen_size
screen_height = min_screen_size

# Set the screen size
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

square_size = screen_width // NB_SQUARES_SIDE

def absolute_pos_to_square_pos(pos):
    return (int(pos[1] // square_size), int(pos[0] // square_size))

def square_pos_to_absolute_pos(pos):
    return (pos[1] * square_size, pos[0] * square_size)

def get_square_from_pos(pos):
    return (int(pos[1] // square_size), int(pos[0] // square_size))

def get_square_color_from_pos(pos):
    square_pos = get_square_from_pos(pos)
    color = screen.get_at((int(square_pos[1] * square_size), int(square_pos[0] * square_size)))[:3] 
    return color

def get_player_from_pos(pos):
    color = screen.get_at((pos[0], pos[1]))[:3]
    if color == PLAYER_1_COLOR:
        return 1
    elif color == PLAYER_2_COLOR:
        return 2
    else:
        return 0

def get_player_color(player):
    if player == 1:
        return PLAYER_1_COLOR
    elif player == 2:
        return PLAYER_2_COLOR
    else:
        return None

def move_piece(pos, new_pos):
    start_square_color = get_square_color_from_pos(pos)
    start_square_pos = get_square_from_pos(pos)

    player = get_player_from_pos(pos)
    player_color = get_player_color(player)
    
    end_square_pos = get_square_from_pos(new_pos)

    pygame.draw.rect(screen, start_square_color, (start_square_pos[1] * square_size, start_square_pos[0] * square_size, square_size, square_size))
    pygame.draw.circle(screen, player_color, (end_square_pos[1] * square_size + square_size // 2, end_square_pos[0] * square_size + square_size // 2), square_size // 2 - PIECE_TO_SQUARE_MARGIN)

def pos_in_board(pos):
    return pos[0] >= 0 and pos[0] < NB_SQUARES_SIDE and pos[1] >= 0 and pos[1] < NB_SQUARES_SIDE

def is_diagonal_move(start_square_pos, end_square_pos):
    return abs(end_square_pos[0] - start_square_pos[0]) == abs(end_square_pos[1] - start_square_pos[1])

def is_empty_square(pos):
    return get_player_from_pos(pos) == 0

def move_length(start_square_pos, end_square_pos):
    return abs(end_square_pos[0] - start_square_pos[0])

def is_valid_move_on_empty_square(new_pos, start_square_color, start_square_pos, end_square_pos):
    return (
            pos_in_board(end_square_pos) 
        and is_diagonal_move(start_square_pos, end_square_pos) 
        and start_square_color != BLACK 
        and is_empty_square(new_pos) 
        and move_length(start_square_pos, end_square_pos) == 1
    )

def get_move_direction(start_square_pos, end_square_pos):
    if end_square_pos[0] < start_square_pos[0] and end_square_pos[1] < start_square_pos[1]:
        return Direction.UP_LEFT
    elif end_square_pos[0] < start_square_pos[0] and end_square_pos[1] > start_square_pos[1]:
        return Direction.UP_RIGHT
    elif end_square_pos[0] > start_square_pos[0] and end_square_pos[1] < start_square_pos[1]:
        return Direction.DOWN_LEFT
    elif end_square_pos[0] > start_square_pos[0] and end_square_pos[1] > start_square_pos[1]:
        return Direction.DOWN_RIGHT

def oposite_player_on_path(start_square_pos, end_square_pos):
    absolute_start_pos = square_pos_to_absolute_pos(start_square_pos)
    move_direction = get_move_direction(start_square_pos, end_square_pos)

    if move_direction == Direction.UP_LEFT:
        return get_player_from_pos(absolute_start_pos) != get_player_from_pos((absolute_start_pos[0] - square_size, absolute_start_pos[1] - square_size))
    elif move_direction == Direction.UP_RIGHT:
        return get_player_from_pos(absolute_start_pos) != get_player_from_pos((absolute_start_pos[0] - square_size, absolute_start_pos[1] + square_size))
    elif move_direction == Direction.DOWN_LEFT:
        return get_player_from_pos(absolute_start_pos) != get_player_from_pos((absolute_start_pos[0] + square_size, absolute_start_pos[1] - square_size))
    elif move_direction == Direction.DOWN_RIGHT:
        return get_player_from_pos(absolute_start_pos) != get_player_from_pos((absolute_start_pos[0] + square_size, absolute_start_pos[1] + square_size))
    
def is_valid_jump_move(new_pos, start_square_color, start_square_pos, end_square_pos):
    return (
            pos_in_board(end_square_pos) 
        and is_diagonal_move(start_square_pos, end_square_pos) 
        and start_square_color != BLACK 
        and is_empty_square(new_pos) 
        and move_length(start_square_pos, end_square_pos) == 2
        and oposite_player_on_path(start_square_pos, end_square_pos)
    )

def is_valid_move(pos, new_pos):
    start_square_color = get_square_color_from_pos(pos)
    start_square_pos = get_square_from_pos(pos)
    
    end_square_pos = get_square_from_pos(new_pos)

    return (
           is_valid_move_on_empty_square(new_pos, start_square_color, start_square_pos, end_square_pos)
        or is_valid_jump_move(new_pos, start_square_color, start_square_pos, end_square_pos)
    )

# Init the board
for i in range(NB_SQUARES_SIDE):
    for j in range(NB_SQUARES_SIDE):
        if (i + j) % 2 == 0:
            pygame.draw.rect(screen, WHITE, (i * square_size, j * square_size, square_size, square_size))
        else:
            pygame.draw.rect(screen, BLACK, (i * square_size, j * square_size, square_size, square_size))

# Set pieces
for i in range(NB_SQUARES_SIDE):
    for j in range(NB_SQUARES_SIDE):
        if (i + j) % 2 == 0:
            if j < 3:
                pygame.draw.circle(screen, PLAYER_1_COLOR, (i * square_size + square_size // 2, j * square_size + square_size // 2), square_size // 2 - PIECE_TO_SQUARE_MARGIN)
            elif j > 4:
                pygame.draw.circle(screen, PLAYER_2_COLOR, (i * square_size + square_size // 2, j * square_size + square_size // 2), square_size // 2 - PIECE_TO_SQUARE_MARGIN)

click_count = 0
first_pos = None
second_pos = None

# Run the game loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("###########################")
            print(f"Square pos :{get_square_from_pos(pygame.mouse.get_pos())}")
            print(f"Absolute pos :{pygame.mouse.get_pos()}")

            color = get_square_color_from_pos(pygame.mouse.get_pos())
            if color == WHITE:
                print("White")
            else:
                print("Black")

            player = get_player_from_pos(pygame.mouse.get_pos())
            if player == 1:
                print("Player 1")
            elif player == 2:
                print("Player 2")
            else:
                print("No player")

            if click_count == 0:
                first_pos = pygame.mouse.get_pos()
                click_count += 1
            else:
                second_pos = pygame.mouse.get_pos()
                click_count += 1

                if click_count == 2:
                    if is_valid_move(first_pos, second_pos):
                        move_piece(first_pos, second_pos)
                    click_count = 0

            print("###########################")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()