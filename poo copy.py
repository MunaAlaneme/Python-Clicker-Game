import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Critical Hit Demo")

# Font and Colors
font = pygame.font.SysFont('arial', 36, bold=True)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock for frame rate
clock = pygame.time.Clock()

# Critical hit effect timer
hit_timer = 0
hit_duration = 1000  # in milliseconds
hit_position = None

running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            hit_timer = pygame.time.get_ticks()
            hit_position = (
                random.randint(50, WIDTH - 200),  # Leave space for text
                random.randint(50, HEIGHT - 50)
            )

    # Display critical hit if within duration
    if hit_position and pygame.time.get_ticks() - hit_timer < hit_duration:
        text = font.render("CRITICAL HIT!", True, RED)
        screen.blit(text, hit_position)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
