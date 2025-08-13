import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Project")
clock = pygame.time.Clock()

# Game variables
running = True

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Game logic goes here
    
    # Drawing
    screen.fill(BLACK)  # Clear screen
    
    # Draw your game objects here
    # Example: pygame.draw.rect(screen, RED, (100, 100, 50, 50))
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
