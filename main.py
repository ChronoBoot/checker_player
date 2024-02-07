import pygame

NB_SQUARES_SIDE = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PIECE_TO_SQUARE_MARGIN = 5

PLAYER_1_COLOR = RED
PLAYER_2_COLOR = BLUE
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
            print(get_square_from_pos(pygame.mouse.get_pos()))

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
                    move_piece(first_pos, second_pos)
                    click_count = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()