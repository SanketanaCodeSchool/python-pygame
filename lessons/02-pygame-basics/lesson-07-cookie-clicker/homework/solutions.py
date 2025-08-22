# Cookie Clicker Enhanced - Complete Solution
# This file contains a fully functional enhanced version of the Cookie Clicker game

import pygame
import sys
import os
import json
import math
import time
from typing import List, Dict, Tuple

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# ============================================================================
# CONSTANTS AND CONFIGURATION
# ============================================================================

# Screen and Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# UI Constants
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
COOKIE_SIZE = 200

# Positions
COOKIE_X = 300
COOKIE_Y = 200
AUTO_CLICKER_BUTTON_X = 550
AUTO_CLICKER_BUTTON_Y = 350
FACTORY_BUTTON_X = 550
FACTORY_BUTTON_Y = 420

# Text positions
TITLE_Y = 30
COOKIE_COUNT_Y = 80
CPS_Y = 110
AUTO_CLICKER_INFO_Y = 350
FACTORY_INFO_Y = 420
MESSAGE_Y = 570

# Colors
GRAY = (190, 190, 190)
DARK_GRAY = (64, 64, 64)
GREEN = (50, 205, 50)
BLUE = (30, 144, 255)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
PURPLE = (147, 112, 219)

# Game States
STATE_PLAYING = "playing"
STATE_ACHIEVEMENTS = "achievements"
STATE_STATS = "stats"

# Achievement definitions
ACHIEVEMENTS = {
    "first_click": {"name": "First Click", "description": "Click the cookie for the first time", "trigger": "click"},
    "cookie_collector": {"name": "Cookie Collector", "description": "Reach 100 cookies", "trigger": "cookies", "threshold": 100},
    "auto_clicker_master": {"name": "Auto-Clicker Master", "description": "Own 10 auto-clickers", "trigger": "auto_clickers", "threshold": 10},
    "factory_owner": {"name": "Factory Owner", "description": "Own 5 factories", "trigger": "factories", "threshold": 5},
    "millionaire": {"name": "Millionaire", "description": "Reach 1000 cookies", "trigger": "cookies", "threshold": 1000},
    "speed_demon": {"name": "Speed Demon", "description": "Reach 50 cookies per second", "trigger": "cps", "threshold": 50}
}

# ============================================================================
# GAME VARIABLES
# ============================================================================

# Core game variables
cookies = 0
cookies_per_click = 1
cookies_per_second = 0
total_cookies_earned = 0
total_clicks = 0
game_start_time = time.time()

# Upgrade system
auto_clickers = 0
factories = 0
auto_clicker_cost = 50
factory_cost = 100

# Animation variables
cookie_scale = 1.0
cookie_animation_time = 0
floating_texts = []  # List of (text, x, y, time, color) tuples
sparkles = []  # List of sparkle particles
button_hover = None

# Audio system
volume = 0.5
muted = False
click_sound = None
purchase_sound = None
background_music = None

# Achievement system
achievements_earned = set()
achievement_notifications = []  # List of (text, time) tuples

# Statistics
highest_cps = 0
start_time = time.time()

# Game state
game_state = STATE_PLAYING

# ============================================================================
# SETUP AND INITIALIZATION
# ============================================================================

def initialize_game():
    """Initialize the game, load assets, and set up the display"""
    global screen, clock, font, cookie_image, background_image
    global click_sound, purchase_sound, background_music
    
    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cookie Clicker Enhanced")
    clock = pygame.time.Clock()
    
    # Fonts
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    # Load assets
    assets_folder = "assets"
    
    # Load images
    cookie_image = pygame.image.load(os.path.join(assets_folder, "cookie.png"))
    cookie_image = pygame.transform.scale(cookie_image, (COOKIE_SIZE, COOKIE_SIZE))
    
    background_image = pygame.image.load(os.path.join(assets_folder, "bg.png"))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Load sounds
    try:
        click_sound = pygame.mixer.Sound(os.path.join(assets_folder, "click.wav"))
        click_sound.set_volume(volume)
    except:
        print("Warning: click.wav not found")
        click_sound = None
    
    try:
        purchase_sound = pygame.mixer.Sound(os.path.join(assets_folder, "purchase.wav"))
        purchase_sound.set_volume(volume)
    except:
        print("Warning: purchase.wav not found")
        purchase_sound = None
    
    try:
        pygame.mixer.music.load(os.path.join(assets_folder, "background_music.mp3"))
        pygame.mixer.music.set_volume(volume * 0.3)  # Background music quieter
        pygame.mixer.music.play(-1)  # Loop
    except:
        print("Warning: background_music.mp3 not found")
    
    # Load saved game
    load_game()

# ============================================================================
# SAVE/LOAD SYSTEM
# ============================================================================

def save_game():
    """Save the current game state to a JSON file"""
    save_data = {
        "cookies": cookies,
        "cookies_per_click": cookies_per_click,
        "cookies_per_second": cookies_per_second,
        "total_cookies_earned": total_cookies_earned,
        "total_clicks": total_clicks,
        "auto_clickers": auto_clickers,
        "factories": factories,
        "auto_clicker_cost": auto_clicker_cost,
        "factory_cost": factory_cost,
        "achievements_earned": list(achievements_earned),
        "highest_cps": highest_cps,
        "start_time": start_time
    }
    
    try:
        with open("cookie_clicker_save.json", "w") as f:
            json.dump(save_data, f)
        show_message("Game saved!", GREEN, 2.0)
    except Exception as e:
        show_message("Failed to save game!", RED, 2.0)
        print(f"Save error: {e}")

def load_game():
    """Load game state from JSON file"""
    global cookies, cookies_per_click, cookies_per_second, total_cookies_earned
    global total_clicks, auto_clickers, factories, auto_clicker_cost, factory_cost
    global achievements_earned, highest_cps, start_time
    
    try:
        with open("cookie_clicker_save.json", "r") as f:
            save_data = json.load(f)
        
        cookies = save_data.get("cookies", 0)
        cookies_per_click = save_data.get("cookies_per_click", 1)
        cookies_per_second = save_data.get("cookies_per_second", 0)
        total_cookies_earned = save_data.get("total_cookies_earned", 0)
        total_clicks = save_data.get("total_clicks", 0)
        auto_clickers = save_data.get("auto_clickers", 0)
        factories = save_data.get("factories", 0)
        auto_clicker_cost = save_data.get("auto_clicker_cost", 50)
        factory_cost = save_data.get("factory_cost", 100)
        achievements_earned = set(save_data.get("achievements_earned", []))
        highest_cps = save_data.get("highest_cps", 0)
        start_time = save_data.get("start_time", time.time())
        
        show_message("Game loaded!", GREEN, 2.0)
    except FileNotFoundError:
        show_message("No save file found. Starting new game.", YELLOW, 2.0)
    except Exception as e:
        show_message("Failed to load game!", RED, 2.0)
        print(f"Load error: {e}")

# ============================================================================
# AUDIO SYSTEM
# ============================================================================

def play_sound(sound):
    """Play a sound effect if not muted"""
    if sound and not muted:
        sound.play()

def toggle_mute():
    """Toggle mute state and update audio"""
    global muted, volume
    
    muted = not muted
    if muted:
        pygame.mixer.music.pause()
        show_message("Audio muted", YELLOW, 1.5)
    else:
        pygame.mixer.music.unpause()
        show_message("Audio unmuted", GREEN, 1.5)

def set_volume(new_volume):
    """Set audio volume"""
    global volume
    volume = max(0.0, min(1.0, new_volume))
    
    if click_sound:
        click_sound.set_volume(volume)
    if purchase_sound:
        purchase_sound.set_volume(volume)
    pygame.mixer.music.set_volume(volume * 0.3)

# ============================================================================
# ANIMATION SYSTEM
# ============================================================================

def update_animations(delta_time):
    """Update all animations and visual effects"""
    global cookie_scale, cookie_animation_time
    
    # Cookie bounce animation
    if cookie_animation_time > 0:
        cookie_animation_time -= delta_time
        cookie_scale = 1.0 + 0.2 * (cookie_animation_time / 0.1)  # 0.1 second animation
    else:
        cookie_scale = 1.0
    
    # Update floating texts
    for i in range(len(floating_texts) - 1, -1, -1):
        text, x, y, time_left, color = floating_texts[i]
        time_left -= delta_time
        if time_left <= 0:
            floating_texts.pop(i)
        else:
            floating_texts[i] = (text, x, y - delta_time * 50, time_left, color)  # Move up
    
    # Update sparkles
    for i in range(len(sparkles) - 1, -1, -1):
        sparkle = sparkles[i]
        sparkle["time"] -= delta_time
        if sparkle["time"] <= 0:
            sparkles.pop(i)
        else:
            sparkle["x"] += sparkle["dx"] * delta_time
            sparkle["y"] += sparkle["dy"] * delta_time
            sparkle["alpha"] = int(255 * (sparkle["time"] / sparkle["max_time"]))

def add_floating_text(text, x, y, color=GREEN, duration=1.0):
    """Add floating text animation"""
    floating_texts.append((text, x, y, duration, color))

def add_sparkles(x, y, count=5):
    """Add sparkle particles around a position"""
    for _ in range(count):
        sparkle = {
            "x": x + (pygame.random.randint(-20, 20)),
            "y": y + (pygame.random.randint(-20, 20)),
            "dx": pygame.random.randint(-50, 50),
            "dy": pygame.random.randint(-100, -20),
            "time": 1.0,
            "max_time": 1.0,
            "alpha": 255
        }
        sparkles.append(sparkle)

def trigger_cookie_animation():
    """Trigger the cookie bounce animation"""
    global cookie_animation_time
    cookie_animation_time = 0.1

# ============================================================================
# ACHIEVEMENT SYSTEM
# ============================================================================

def check_achievements():
    """Check and award achievements based on current game state"""
    global achievements_earned
    
    # Check each achievement
    for achievement_id, achievement in ACHIEVEMENTS.items():
        if achievement_id in achievements_earned:
            continue  # Already earned
        
        earned = False
        trigger = achievement["trigger"]
        
        if trigger == "click" and total_clicks == 1:
            earned = True
        elif trigger == "cookies" and cookies >= achievement["threshold"]:
            earned = True
        elif trigger == "auto_clickers" and auto_clickers >= achievement["threshold"]:
            earned = True
        elif trigger == "factories" and factories >= achievement["threshold"]:
            earned = True
        elif trigger == "cps" and cookies_per_second >= achievement["threshold"]:
            earned = True
        
        if earned:
            achievements_earned.add(achievement_id)
            show_achievement_notification(achievement["name"])

def show_achievement_notification(achievement_name):
    """Show an achievement notification"""
    notification_text = f"Achievement Unlocked: {achievement_name}!"
    achievement_notifications.append((notification_text, 3.0))
    show_message(notification_text, YELLOW, 3.0)

def update_achievement_notifications(delta_time):
    """Update achievement notification timers"""
    for i in range(len(achievement_notifications) - 1, -1, -1):
        text, time_left = achievement_notifications[i]
        time_left -= delta_time
        if time_left <= 0:
            achievement_notifications.pop(i)
        else:
            achievement_notifications[i] = (text, time_left)

# ============================================================================
# UPGRADE SYSTEM
# ============================================================================

def buy_auto_clicker():
    """Purchase an auto-clicker upgrade"""
    global cookies, auto_clickers, auto_clicker_cost, cookies_per_second
    
    if cookies >= auto_clicker_cost:
        cookies -= auto_clicker_cost
        auto_clickers += 1
        cookies_per_second += 1
        auto_clicker_cost = int(auto_clicker_cost * 1.2)  # 20% increase
        
        play_sound(purchase_sound)
        add_sparkles(AUTO_CLICKER_BUTTON_X + BUTTON_WIDTH//2, AUTO_CLICKER_BUTTON_Y + BUTTON_HEIGHT//2)
        show_message(f"Auto-Clicker purchased! ({auto_clickers} owned)", GREEN, 1.5)
        return True
    else:
        show_message("Not enough cookies!", RED, 1.0)
        return False

def buy_factory():
    """Purchase a factory upgrade"""
    global cookies, factories, factory_cost, cookies_per_second
    
    if cookies >= factory_cost:
        cookies -= factory_cost
        factories += 1
        cookies_per_second += 5
        factory_cost = int(factory_cost * 1.2)  # 20% increase
        
        play_sound(purchase_sound)
        add_sparkles(FACTORY_BUTTON_X + BUTTON_WIDTH//2, FACTORY_BUTTON_Y + BUTTON_HEIGHT//2)
        show_message(f"Factory purchased! ({factories} owned)", GREEN, 1.5)
        return True
    else:
        show_message("Not enough cookies!", RED, 1.0)
        return False

# ============================================================================
# UI RENDERING
# ============================================================================

def create_button(text, x, y, width, height, color, hover_color=None):
    """Create a button with hover effect"""
    button_rect = pygame.Rect(x, y, width, height)
    
    # Check if mouse is hovering
    mouse_pos = pygame.mouse.get_pos()
    is_hovering = button_rect.collidepoint(mouse_pos)
    
    # Choose color based on hover state
    button_color = hover_color if is_hovering and hover_color else color
    
    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, DARK_GRAY, button_rect, 2)
    
    text_surface = font.render(text, True, DARK_GRAY)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    
    return button_rect

def draw_text(text, x, y, color=GRAY, font_obj=None):
    """Draw text at specified position"""
    if font_obj is None:
        font_obj = font
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_cookie():
    """Draw the cookie with animation"""
    # Scale the cookie image
    scaled_size = int(COOKIE_SIZE * cookie_scale)
    scaled_cookie = pygame.transform.scale(cookie_image, (scaled_size, scaled_size))
    
    # Center the scaled cookie
    x_offset = (scaled_size - COOKIE_SIZE) // 2
    y_offset = (scaled_size - COOKIE_SIZE) // 2
    
    screen.blit(scaled_cookie, (COOKIE_X - x_offset, COOKIE_Y - y_offset))

def draw_floating_texts():
    """Draw all floating text animations"""
    for text, x, y, time_left, color in floating_texts:
        alpha = int(255 * (time_left / 1.0))  # Fade out
        color_with_alpha = (*color, alpha)
        draw_text(text, x, y, color)

def draw_sparkles():
    """Draw sparkle particles"""
    for sparkle in sparkles:
        alpha = sparkle["alpha"]
        color = (255, 255, 255, alpha)
        # Draw a simple sparkle (white dot)
        pygame.draw.circle(screen, (255, 255, 255), 
                         (int(sparkle["x"]), int(sparkle["y"])), 2)

def draw_achievement_notifications():
    """Draw achievement notifications"""
    y_offset = 50
    for text, time_left in achievement_notifications:
        alpha = int(255 * (time_left / 3.0))
        draw_text(text, SCREEN_WIDTH // 2, y_offset, YELLOW)
        y_offset += 30

def draw_main_screen():
    """Draw the main game screen"""
    # Background
    screen.blit(background_image, (0, 0))
    
    # Title and stats
    draw_text("Cookie Clicker Enhanced", SCREEN_WIDTH // 2, TITLE_Y)
    draw_text(f"Cookies: {cookies:,}", SCREEN_WIDTH // 2, COOKIE_COUNT_Y)
    draw_text(f"Cookies per second: {cookies_per_second}", SCREEN_WIDTH // 2, CPS_Y)
    
    # Cookie
    draw_cookie()
    
    # Upgrade buttons
    auto_clicker_rect = create_button(
        f"Auto-Clicker ({auto_clicker_cost})", 
        AUTO_CLICKER_BUTTON_X, AUTO_CLICKER_BUTTON_Y, 
        BUTTON_WIDTH, BUTTON_HEIGHT, BLUE, (100, 150, 255)
    )
    
    factory_rect = create_button(
        f"Factory ({factory_cost})", 
        FACTORY_BUTTON_X, FACTORY_BUTTON_Y, 
        BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, (100, 255, 100)
    )
    
    # Upgrade info
    draw_text(f"Auto-Clickers: {auto_clickers}", SCREEN_WIDTH // 2, AUTO_CLICKER_INFO_Y + 30)
    draw_text(f"Factories: {factories}", SCREEN_WIDTH // 2, FACTORY_INFO_Y + 30)
    
    # Instructions
    draw_text("Click the cookie to earn cookies! Press S to save, L to load, M to mute", 
             SCREEN_WIDTH // 2, MESSAGE_Y, small_font)
    
    # Draw animations
    draw_floating_texts()
    draw_sparkles()
    draw_achievement_notifications()
    
    return auto_clicker_rect, factory_rect

def draw_achievements_screen():
    """Draw the achievements screen"""
    screen.blit(background_image, (0, 0))
    
    draw_text("Achievements", SCREEN_WIDTH // 2, 50)
    
    y_offset = 120
    for achievement_id, achievement in ACHIEVEMENTS.items():
        color = YELLOW if achievement_id in achievements_earned else GRAY
        status = "✓" if achievement_id in achievements_earned else "✗"
        
        draw_text(f"{status} {achievement['name']}", 100, y_offset, color, small_font)
        draw_text(achievement['description'], 400, y_offset, color, small_font)
        y_offset += 40
    
    draw_text("Press any key to return", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

def draw_stats_screen():
    """Draw the statistics screen"""
    screen.blit(background_image, (0, 0))
    
    draw_text("Statistics", SCREEN_WIDTH // 2, 50)
    
    play_time = time.time() - start_time
    hours = int(play_time // 3600)
    minutes = int((play_time % 3600) // 60)
    seconds = int(play_time % 60)
    
    stats = [
        f"Total Cookies Earned: {total_cookies_earned:,}",
        f"Total Clicks: {total_clicks:,}",
        f"Play Time: {hours:02d}:{minutes:02d}:{seconds:02d}",
        f"Highest CPS: {highest_cps}",
        f"Achievements Earned: {len(achievements_earned)}/{len(ACHIEVEMENTS)}",
        f"Current CPS: {cookies_per_second}",
        f"Auto-Clickers Owned: {auto_clickers}",
        f"Factories Owned: {factories}"
    ]
    
    y_offset = 120
    for stat in stats:
        draw_text(stat, SCREEN_WIDTH // 2, y_offset)
        y_offset += 40
    
    draw_text("Press any key to return", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

# ============================================================================
# MESSAGE SYSTEM
# ============================================================================

messages = []  # List of (text, time_left, color) tuples

def show_message(text, color=GREEN, duration=2.0):
    """Show a temporary message on screen"""
    messages.append((text, duration, color))

def update_messages(delta_time):
    """Update message timers"""
    for i in range(len(messages) - 1, -1, -1):
        text, time_left, color = messages[i]
        time_left -= delta_time
        if time_left <= 0:
            messages.pop(i)
        else:
            messages[i] = (text, time_left, color)

def draw_messages():
    """Draw all active messages"""
    y_offset = 150
    for text, time_left, color in messages:
        alpha = int(255 * (time_left / 2.0))
        draw_text(text, SCREEN_WIDTH // 2, y_offset, color)
        y_offset += 30

# ============================================================================
# GAME LOGIC
# ============================================================================

def handle_click(mouse_pos):
    """Handle mouse clicks based on current game state"""
    global cookies, total_cookies_earned, total_clicks, highest_cps
    
    if game_state == STATE_PLAYING:
        # Check cookie click
        cookie_rect = pygame.Rect(COOKIE_X, COOKIE_Y, COOKIE_SIZE, COOKIE_SIZE)
        if cookie_rect.collidepoint(mouse_pos):
            cookies += cookies_per_click
            total_cookies_earned += cookies_per_click
            total_clicks += 1
            
            play_sound(click_sound)
            trigger_cookie_animation()
            add_floating_text(f"+{cookies_per_click}", mouse_pos[0], mouse_pos[1])
            
            # Check for highest CPS
            if cookies_per_second > highest_cps:
                highest_cps = cookies_per_second
            
            return
        
        # Check upgrade button clicks
        auto_clicker_rect = pygame.Rect(AUTO_CLICKER_BUTTON_X, AUTO_CLICKER_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        if auto_clicker_rect.collidepoint(mouse_pos):
            buy_auto_clicker()
            return
        
        factory_rect = pygame.Rect(FACTORY_BUTTON_X, FACTORY_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
        if factory_rect.collidepoint(mouse_pos):
            buy_factory()
            return

def update_game(delta_time):
    """Update game state and logic"""
    global cookies, total_cookies_earned
    
    # Auto-generate cookies
    auto_cookies = cookies_per_second * delta_time
    cookies += auto_cookies
    total_cookies_earned += auto_cookies
    
    # Update animations
    update_animations(delta_time)
    
    # Check achievements
    check_achievements()
    
    # Update notifications
    update_achievement_notifications(delta_time)
    update_messages(delta_time)

# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def main():
    """Main game loop"""
    global game_state
    
    initialize_game()
    
    running = True
    last_time = time.time()
    
    while running:
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_s:
                    save_game()
                elif event.key == pygame.K_l:
                    load_game()
                elif event.key == pygame.K_m:
                    toggle_mute()
                elif event.key == pygame.K_a:
                    game_state = STATE_ACHIEVEMENTS if game_state == STATE_PLAYING else STATE_PLAYING
                elif event.key == pygame.K_t:
                    game_state = STATE_STATS if game_state == STATE_PLAYING else STATE_PLAYING
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if game_state == STATE_PLAYING:
                        handle_click(event.pos)
                    elif game_state in [STATE_ACHIEVEMENTS, STATE_STATS]:
                        game_state = STATE_PLAYING
        
        # Update game logic
        if game_state == STATE_PLAYING:
            update_game(delta_time)
        
        # Drawing
        if game_state == STATE_PLAYING:
            draw_main_screen()
            draw_messages()
        elif game_state == STATE_ACHIEVEMENTS:
            draw_achievements_screen()
        elif game_state == STATE_STATS:
            draw_stats_screen()
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    # Save game before quitting
    save_game()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
