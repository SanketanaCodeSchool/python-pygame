import pygame
import sys
import os
import json

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 144  # Higher FPS for better responsiveness

# UI Constants
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
COOKIE_SIZE = 200

# Button positions
START_BUTTON_X = 300
START_BUTTON_Y = 300

# Cookie position
COOKIE_X = 300
COOKIE_Y = 200

# Text positions
TITLE_Y = 30
COOKIE_COUNT_Y = 80
TARGET_Y = 110
PER_CLICK_Y = 420
INSTRUCTIONS_Y = 570

# Start screen text positions
START_TITLE_Y = 150
START_INSTRUCTION1_Y = 250
START_INSTRUCTION2_Y = 280

# Win screen text positions
WIN_TITLE_Y = 150
WIN_SUBTITLE_Y = 200
WIN_SCORE_Y = 250
WIN_TARGET_Y = 280

# Colors
GRAY = (190, 190, 190)  # Lighter gray for better contrast
DARK_GRAY = (64, 64, 64)
GREEN = (50, 205, 50)  # Vibrant green like "Per Click" text
BLUE = (30, 144, 255)  # Bright blue for buttons like in screenshot

# Game States
STATE_START = "start"
STATE_PLAYING = "playing"
STATE_WIN = "win"

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cookie Clicker")
clock = pygame.time.Clock()

# Fonts - using only one font size
font = pygame.font.Font(None, 36)

# Game variables
cookies = 0
cookies_per_click = 1
target_cookies = 100  # Win condition
game_state = STATE_START
last_mouse_state = False  # Track mouse button state

# Load assets directly
assets_folder = "assets"

# Load cookie image
cookie_image = pygame.image.load(os.path.join(assets_folder, "cookie.png"))
cookie_image = pygame.transform.scale(cookie_image, (200, 200))

# Load background image
background_image = pygame.image.load(os.path.join(assets_folder, "bg.png"))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load sounds
click_sound = pygame.mixer.Sound(os.path.join(assets_folder, "snap.wav"))
click_sound.set_volume(0.5)

# Load background music
pygame.mixer.music.load(os.path.join(assets_folder, "bg_score.mp3"))
pygame.mixer.music.set_volume(0.2)

# Create button - simplified without hover color
def create_button(text, x, y, width, height, color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, DARK_GRAY, button_rect, 2)
    
    text_surface = font.render(text, True, DARK_GRAY)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    
    return button_rect

# Draw text - using single font and color
def draw_text(text, x, y):
    text_surface = font.render(text, True, GRAY)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Reset game
def reset_game():
    global cookies, game_state
    cookies = 0
    game_state = STATE_START

# Screen drawing functions
def draw_start_screen():
    draw_text("Cookie Clicker", SCREEN_WIDTH // 2, START_TITLE_Y)
    draw_text("Click the cookie to earn cookies!", SCREEN_WIDTH // 2, START_INSTRUCTION1_Y)
    draw_text("Reach 100 cookies to win!", SCREEN_WIDTH // 2, START_INSTRUCTION2_Y)
    
    start_button_rect = create_button("Start Game", START_BUTTON_X, START_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, GREEN)
    return start_button_rect

def draw_playing_screen():
    draw_text("Cookie Clicker", SCREEN_WIDTH // 2, TITLE_Y)
    
    # Draw cookie count
    draw_text(f"Cookies: {cookies}", SCREEN_WIDTH // 2, COOKIE_COUNT_Y)
    draw_text(f"Target: {target_cookies}", SCREEN_WIDTH // 2, TARGET_Y)
    
    # Draw cookie
    screen.blit(cookie_image, (COOKIE_X, COOKIE_Y))
    
   
    # Draw instructions
    draw_text("Click the cookie to earn cookies!", SCREEN_WIDTH // 2, INSTRUCTIONS_Y)

def draw_win_screen():
    draw_text("Congratulations!", SCREEN_WIDTH // 2, WIN_TITLE_Y)
    draw_text("You won!", SCREEN_WIDTH // 2, WIN_SUBTITLE_Y)
    draw_text(f"You collected {cookies} cookies!", SCREEN_WIDTH // 2, WIN_SCORE_Y)
    draw_text("You reached the target of 100 cookies!", SCREEN_WIDTH // 2, WIN_TARGET_Y)
    
    replay_button_rect = create_button("Play Again", START_BUTTON_X, START_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, BLUE)
    return replay_button_rect

# Mouse event handling functions
def handle_start_screen_click(mouse_pos):
    global game_state
    start_button_rect = pygame.Rect(START_BUTTON_X, START_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    if start_button_rect.collidepoint(mouse_pos):
        game_state = STATE_PLAYING

def handle_playing_screen_click(mouse_pos):
    global cookies, game_state
    cookie_rect = pygame.Rect(COOKIE_X, COOKIE_Y, COOKIE_SIZE, COOKIE_SIZE)
    if cookie_rect.collidepoint(mouse_pos):
        cookies += cookies_per_click
        
        # Play click sound
        click_sound.play()
        
        # Check win condition
        if cookies >= target_cookies:
            game_state = STATE_WIN

def handle_win_screen_click(mouse_pos):
    replay_button_rect = pygame.Rect(START_BUTTON_X, START_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
    if replay_button_rect.collidepoint(mouse_pos):
        reset_game()

# Start background music
pygame.mixer.music.play(-1)  # Loop background music

# Game loop
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # More responsive mouse input handling
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    current_mouse_state = mouse_buttons[0]  # Left mouse button
    
    # Check for mouse button press (not just click)
    if current_mouse_state and not last_mouse_state:
        if game_state == STATE_START:
            handle_start_screen_click(mouse_pos)
        elif game_state == STATE_PLAYING:
            handle_playing_screen_click(mouse_pos)
        elif game_state == STATE_WIN:
            handle_win_screen_click(mouse_pos)
    
    last_mouse_state = current_mouse_state
    
    # Drawing
    # Draw background
    screen.blit(background_image, (0, 0))
    
    if game_state == STATE_START:
        draw_start_screen()
    elif game_state == STATE_PLAYING:
        draw_playing_screen()
    elif game_state == STATE_WIN:
        draw_win_screen()
    
    # Update display
    pygame.display.flip()
    
    # No frame rate limiting for maximum responsiveness
    # clock.tick(FPS)

# Clean up
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
