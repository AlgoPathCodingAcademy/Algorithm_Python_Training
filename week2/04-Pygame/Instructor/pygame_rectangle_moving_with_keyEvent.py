import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Horizontal Bouncing Rectangle")

# Rectangle properties
rect_color = (255, 0, 0)  # Red color
rect_x, rect_y = 100, 250  # Initial position of the rectangle
rect_width, rect_height = 200, 100  # Size of the rectangle
rect_speed_x = 5  # Horizontal movement speed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Check if the 'Q' key is pressed
                running = False

    # Update the rectangle's position
    rect_x += rect_speed_x

    # Bounce the rectangle off the horizontal edges of the window
    if rect_x + rect_width > window_width or rect_x < 0:
        rect_speed_x *= -1

    # Clear the window
    window.fill((0, 0, 0))  # Fill with black color

    # Draw the rectangle on the main surface
    pygame.draw.rect(window, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
