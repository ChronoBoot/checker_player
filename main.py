import pygame

NB_SQUARES_SIDE = 8
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

square_size = screen_width / NB_SQUARES_SIDE

# Init the board
for i in range(NB_SQUARES_SIDE):
    for j in range(NB_SQUARES_SIDE):
        if (i + j) % 2 == 0:
            pygame.draw.rect(screen, (255, 255, 255), (i * square_size, j * square_size, square_size, square_size))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (i * square_size, j * square_size, square_size, square_size))

# Run the game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()