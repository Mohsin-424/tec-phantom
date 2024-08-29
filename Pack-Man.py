import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Pac-Man settings
pacman_size = 40
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 5

# Ghost settings
ghost_size = 40
ghost_x = random.randint(0, WIDTH - ghost_size)
ghost_y = random.randint(0, HEIGHT - ghost_size)
ghost_speed = 3

# Dot settings
dot_size = 10
dots = [(random.randint(0, WIDTH - dot_size), random.randint(0, HEIGHT - dot_size)) for _ in range(20)]

# Main game loop
running = True
while running:
    clock.tick(30)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Move the ghost
    if pacman_x > ghost_x:
        ghost_x += ghost_speed
    if pacman_x < ghost_x:
        ghost_x -= ghost_speed
    if pacman_y > ghost_y:
        ghost_y += ghost_speed
    if pacman_y < ghost_y:
        ghost_y -= ghost_speed

    # Check collision with ghost
    if (abs(pacman_x - ghost_x) < pacman_size and
            abs(pacman_y - ghost_y) < pacman_size):
        print("Pac-Man caught by ghost!")
        running = False

    # Check collision with dots
    dots = [dot for dot in dots if not (pacman_x < dot[0] < pacman_x + pacman_size and pacman_y < dot[1] < pacman_y + pacman_size)]

    # Draw everything
    win.fill(BLACK)
    pygame.draw.rect(win, YELLOW, (pacman_x, pacman_y, pacman_size, pacman_size))
    pygame.draw.rect(win, WHITE, (ghost_x, ghost_y, ghost_size, ghost_size))
    for dot in dots:
        pygame.draw.circle(win, WHITE, dot, dot_size)

    pygame.display.update()

# Quit pygame
pygame.quit()
