import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Heroes with Image")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Game variables
enemy_hp = 100
enemy_max_hp = 100
gold = 0
click_damage = 10
hit_timer = 0

# Load and scale enemy image
enemy_image = pygame.image.load("assets/img/copilot.png").convert_alpha()
enemy_image_original = pygame.transform.scale(enemy_image, (100, 100))
enemy_rect = enemy_image_original.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Colors
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
BLACK = (0, 0, 0)

# Game loop
running = True
pygame.mixer.init(11025, 8, 2, 512)
pygame.mixer.music.load("./assets/audio/Kevin MacLeod - Hep Cats.mp3")
pygame.mixer.music.play(-1)
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if enemy_rect.collidepoint(event.pos):
                enemy_hp -= click_damage
                hit_timer = 5
                if enemy_hp <= 0:
                    gold += random.randint(5, 15)
                    enemy_hp = enemy_max_hp + 10
                    enemy_max_hp = enemy_hp

    # Animate hit (scale slightly)
    if hit_timer > 0:
        scaled_image = pygame.transform.scale(enemy_image, (90, 90))
        hit_timer -= 1
    else:
        scaled_image = enemy_image_original

    # Center the scaled image
    scaled_rect = scaled_image.get_rect(center=enemy_rect.center)

    # Draw enemy image
    screen.blit(scaled_image, scaled_rect)

    # Draw HP bar
    hp_bar_width = 100 * (enemy_hp / enemy_max_hp)
    pygame.draw.rect(screen, GREEN, (enemy_rect.x, enemy_rect.y - 20, hp_bar_width, 10))

    # Draw UI
    hp_text = font.render(f"HP: {enemy_hp}/{enemy_max_hp}", True, BLACK)
    gold_text = font.render(f"Gold: {gold}", True, BLACK)
    screen.blit(hp_text, (10, 10))
    screen.blit(gold_text, (10, 50))

    pygame.display.flip()

pygame.quit()