import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player properties
player_size = 20
player_x, player_y = 50, 50
player_speed = 5

# Goal properties
goal_size = 30
goal_x, goal_y = 550, 350

# Maze walls (x, y, width, height)
walls = [
    (100, 0, 20, 300),
    (200, 100, 20, 300),
    (300, 0, 20, 300),
    (400, 100, 20, 300),
    (500, 0, 20, 300),
]

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Player collision with walls
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for wall in walls:
        wall_rect = pygame.Rect(wall)
        if player_rect.colliderect(wall_rect):
            # Reset position if collided
            if keys[pygame.K_UP]:
                player_y += player_speed
            if keys[pygame.K_DOWN]:
                player_y -= player_speed
            if keys[pygame.K_LEFT]:
                player_x += player_speed
            if keys[pygame.K_RIGHT]:
                player_x -= player_speed

    # Check if player reaches the goal
    goal_rect = pygame.Rect(goal_x, goal_y, goal_size, goal_size)
    if player_rect.colliderect(goal_rect):
        print("You Win!")
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)  # Player
    pygame.draw.rect(screen, GREEN, goal_rect)  # Goal
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)  # Walls

    pygame.display.flip()
    clock.tick(30)

pygame.quit()