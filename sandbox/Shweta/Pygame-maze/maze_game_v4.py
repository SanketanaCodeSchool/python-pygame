import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game - Multi-Level Challenge")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Game constants
player_size = 20
player_speed = 5
goal_size = 30

# Initialize player
player_x, player_y = 50, 50

# Score
score = 0

# Clock
clock = pygame.time.Clock()

# Levels data
levels = [
    {  # Level 1
        "walls": [(100, 0, 20, 300), (200, 100, 20, 300)],
        "coins": [(150, 150, 15, 15), (250, 50, 15, 15)],
        "hazards": [[300, 200, 20, 20, 3, 2]],
        "goal": (550, 350),
    },
    {  # Level 2
        "walls": [
            (50, 50, 500, 20),
            (100, 200, 400, 20),
            (200, 100, 20, 200),
        ],
        "coins": [(100, 300, 15, 15), (400, 250, 15, 15)],
        "hazards": [
            [150, 150, 20, 20, -3, 3],
            [450, 50, 20, 20, 3, -2],
        ],
        "goal": (550, 50),
    },
    {  # Level 3
        "walls": [
            (100, 0, 20, 300),
            (200, 100, 20, 300),
            (300, 0, 20, 300),
            (400, 100, 20, 300),
        ],
        "coins": [(150, 50, 15, 15), (250, 350, 15, 15), (450, 200, 15, 15)],
        "hazards": [
            [50, 350, 20, 20, 3, 3],
            [300, 150, 20, 20, -2, 4],
            [500, 100, 20, 20, -4, -3],
        ],
        "goal": (550, 350),
    },
]

current_level = 0

# Main game loop
running = True
while running:
    # Load current level data
    level = levels[current_level]
    walls = level["walls"]
    coins = level["coins"]
    hazards = level["hazards"]
    goal_x, goal_y = level["goal"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
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

        # Collect coins
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
                hazard[4] = -hazard[4]
            if hazard[1] <= 0 or hazard[1] + hazard[3] >= HEIGHT:
                hazard[5] = -hazard[5]

        # Check for hazard collision
        for hazard in hazards:
            hazard_rect = pygame.Rect(hazard[0], hazard[1], hazard[2], hazard[3])
            if player_rect.colliderect(hazard_rect):
                print("Game Over! You hit a hazard!")
                running = False
                pygame.quit()
                sys.exit()

        # Check if player reaches the goal
        goal_rect = pygame.Rect(goal_x, goal_y, goal_size, goal_size)
        if player_rect.colliderect(goal_rect):
            current_level += 1
            if current_level == len(levels):  # Check if last level is completed
                print(f"Congratulations! You completed all levels! Final Score: {score}")
                running = False
            else:
                print(f"Level {current_level} complete! Moving to next level...")
                player_x, player_y = 30, 30  # Reset player position for the next level
            break

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

        # Display score and level
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {current_level + 1}", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        pygame.display.flip()
        clock.tick(30)

pygame.quit()