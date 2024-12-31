import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple FPS Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player properties
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 5

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Enemy properties
enemy_size = 50
enemies = []
enemy_spawn_time = 30  # Spawn an enemy every 30 frames
frame_count = 0

# Score
score = 0

# Font for displaying the score
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        # Fire a bullet
        bullets.append([player_x + player_size // 2, player_y])

    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn enemies
    frame_count += 1
    if frame_count >= enemy_spawn_time:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
        enemies.append([enemy_x, 0])
        frame_count = 0

    # Update enemies
    for enemy in enemies[:]:
        enemy[1] += 3  # Enemy speed
        if enemy[1] > SCREEN_HEIGHT:
            enemies.remove(enemy)
        
        # Check for collisions with bullets
        for bullet in bullets[:]:
            if (
                bullet[0] > enemy[0]
                and bullet[0] < enemy[0] + enemy_size
                and bullet[1] > enemy[1]
                and bullet[1] < enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
