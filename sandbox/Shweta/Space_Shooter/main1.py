import pygame
import random
from os import path

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 480, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooter!")
clock = pygame.time.Clock()

# Load images
background = pygame.image.load("starfield.png").convert()
player_img = pygame.image.load("player.png").convert()
meteor_img = pygame.image.load("enemy.png").convert()
bullet_img = pygame.image.load("bullet.png").convert()

# Load sound
shoot_sound = pygame.mixer.Sound("Laser_Shoot4.wav")

# Player setup
player = {
    "x": WIDTH // 2,
    "y": HEIGHT - 50,
    "speed": 8,
    "image": pygame.transform.scale(player_img, (50, 38))
}
player["image"].set_colorkey(BLACK)

# Enemies setup
def create_enemy():
    return {
        "x": random.randint(0, WIDTH - 40),
        "y": random.randint(-100, -40),
        "speed_x": random.randint(-3, 3),
        "speed_y": random.randint(1, 8),
        "image": pygame.transform.scale(meteor_img, (40, 38)) 
    }

enemies = [create_enemy() for _ in range(8)]
for enemy in enemies:
    enemy["image"].set_colorkey(BLACK)

# Bullets setup
bullets = []
bullet_speed = -10

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append({"x": player["x"] + 25, "y": player["y"], "image": bullet_img})
                shoot_sound.play()
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT]:
        player["x"] += player["speed"]
    player["x"] = max(0, min(WIDTH - 50, player["x"]))
    
    # Bullet movement
    for bullet in bullets:
        bullet["y"] += bullet_speed
    bullets = [b for b in bullets if b["y"] > 0]
    
    # Enemy movement
    for enemy in enemies:
        enemy["x"] += enemy["speed_x"]
        enemy["y"] += enemy["speed_y"]
        if enemy["y"] > HEIGHT or enemy["x"] < -25 or enemy["x"] > WIDTH + 25:
            enemy.update(create_enemy())
    
    # Collision detection
    new_enemies = []
    for enemy in enemies:
        hit = False
        for bullet in bullets:
            if enemy["x"] < bullet["x"] < enemy["x"] + 40 and enemy["y"] < bullet["y"] < enemy["y"] + 40:
                bullets.remove(bullet)
                hit = True
                break
        if hit:
            new_enemies.append(create_enemy())
        else:
            new_enemies.append(enemy)
    enemies = new_enemies
    
    # Check if enemy hits player
    for enemy in enemies:
        if player["x"] < enemy["x"] < player["x"] + 50 and player["y"] < enemy["y"] < player["y"] + 38:
            running = False
    
    # Drawing
    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    screen.blit(player["image"], (player["x"], player["y"]))
    for enemy in enemies:
        screen.blit(enemy["image"], (enemy["x"], enemy["y"]))
    for bullet in bullets:
        screen.blit(bullet["image"], (bullet["x"], bullet["y"]))
    pygame.display.flip()

pygame.quit()
