import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Log Display")

# Set up fonts
font = pygame.font.Font(None, 36)

# Function to display logs
def display_log(message, y_position):
    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (10, y_position))

# Main loop
logs = []
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # For demo: Add logs on key press
        if event.type == pygame.KEYDOWN:
            logs.append(f"Key pressed: {pygame.key.name(event.key)}")
            if len(logs) > 10:  # Limit to 10 log messages
                logs.pop(0)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Display logs
    for i, log in enumerate(logs):
        display_log(log, 10 + i * 30)  # Display each log 30 pixels apart

    # Update the display
    pygame.display.flip()
    clock.tick(60)
