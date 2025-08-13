import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game with Moving Hazards")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

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

# Coins (x, y, width, height)
coins = [
    (150, 150, 15, 15),
    (250, 50, 15, 15),
    (350, 250, 15, 15),
    (450, 150, 15, 15),
]

# Hazards (x, y, width, height, x_speed, y_speed)
hazards = [
    [180, 200, 20, 20, 3, 2],  # Hazard 1: Moves diagonally
    [380, 100, 20, 20, 2, -3],  # Hazard 2: Moves diagonally
]

# Score
score = 0

# Game loop
clock = pygame.time.Clock()

def show_game_over():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.delay(3000)  # Show for 2 seconds before quitting




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

    # Check for coin collection
    collected_coins = []
    for coin in coins:
        coin_rect = pygame.Rect(coin)
        if player_rect.colliderect(coin_rect):
            score += 10
            collected_coins.append(coin)
    coins = [coin for coin in coins if coin not in collected_coins]

    # Move hazards
    for hazard in hazards:
        hazard[0] += hazard[4]  # Update x position
        hazard[1] += hazard[5]  # Update y position

        # Bounce off walls
        if hazard[0] <= 0 or hazard[0] + hazard[2] >= WIDTH:
            hazard[4] = -hazard[4]  # Reverse x direction
        if hazard[1] <= 0 or hazard[1] + hazard[3] >= HEIGHT:
            hazard[5] = -hazard[5]  # Reverse y direction

    # Check for collision with hazards
    for hazard in hazards:
        hazard_rect = pygame.Rect(hazard[0], hazard[1], hazard[2], hazard[3])
        if player_rect.colliderect(hazard_rect):
            show_game_over()
            #print("Game Over! You hit a hazard!")
            running = False

    # Check if player reaches the goal
    goal_rect = pygame.Rect(goal_x, goal_y, goal_size, goal_size)
    if player_rect.colliderect(goal_rect):
        print(f"You Win! Final Score: {score}")
        running = False

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)  # Player
    pygame.draw.rect(screen, GREEN, goal_rect)  # Goal
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)  # Walls
    for coin in coins:
        pygame.draw.rect(screen, YELLOW, coin)  # Coins
    for hazard in hazards:
        pygame.draw.rect(screen, PURPLE, (hazard[0], hazard[1], hazard[2], hazard[3]))  # Hazards

    # Display score
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()