import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Interactive Circle")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Cross properties
line_width = 2
cross_size = 200  # Size of the cross arms

# Font for numbers
font = pygame.font.Font(None, 72)

# Counter for unique key presses
unique_key_presses = 0
key_sequence = set()

# Function to draw quarter circle in a quadrant
def draw_quarter_circle(quadrant):
    if quadrant == 1:
        pygame.draw.arc(screen, black, [center_x - cross_size, center_y - cross_size, cross_size * 2, cross_size * 2], math.radians(90), math.radians(180), line_width)
    elif quadrant == 2:
        pygame.draw.arc(screen, black, [center_x - cross_size, center_y - cross_size, cross_size * 2, cross_size * 2], math.radians(0), math.radians(90), line_width)
    elif quadrant == 3:
        pygame.draw.arc(screen, black, [center_x - cross_size, center_y - cross_size, cross_size * 2, cross_size * 2], math.radians(180), math.radians(270), line_width)
    elif quadrant == 4:
        pygame.draw.arc(screen, black, [center_x - cross_size, center_y - cross_size, cross_size * 2, cross_size * 2], math.radians(270), math.radians(0), line_width)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                key_num = int(pygame.key.name(event.key))
                if key_num not in key_sequence:
                    key_sequence.add(key_num)
                    unique_key_presses += 1

    # Fill the screen with white
    screen.fill(white)

    # Calculate the center of the screen
    center_x, center_y = screen_width // 2, screen_height // 2

    # Draw the cross
    pygame.draw.line(screen, black, (center_x, center_y - cross_size // 2), (center_x, center_y + cross_size // 2), line_width)
    pygame.draw.line(screen, black, (center_x - cross_size // 2, center_y), (center_x + cross_size // 2, center_y), line_width)

    # Draw the quarter circles for completed quadrants
    for quadrant in key_sequence:
        draw_quarter_circle(quadrant)

    # If all four quadrants are marked, fill the circle
    if unique_key_presses == 4:
        pygame.draw.circle(screen, green, (center_x, center_y), cross_size, 0)

    # Render and place numbers
    text1 = font.render('1', True, black)
    text2 = font.render('2', True, black)
    text3 = font.render('3', True, black)
    text4 = font.render('4', True, black)

    screen.blit(text1, (center_x - text1.get_width() - 10, center_y - text1.get_height() - 10))
    screen.blit(text2, (center_x + 10, center_y - text2.get_height() - 10))
    screen.blit(text3, (center_x - text3.get_width() - 10, center_y + 10))
    screen.blit(text4, (center_x + 10, center_y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
