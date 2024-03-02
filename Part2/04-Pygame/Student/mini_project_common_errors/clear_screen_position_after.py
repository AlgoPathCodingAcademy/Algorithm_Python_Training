import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()
window  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Demo")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Check if the 's' key is pressed

              # Define circle properties
              circle_color = (0, 255, 0)  # Green color
              circle_center = (300, 200)  # Center of the screen
              circle_radius = 50          # Radius of the circle
              
              # Draw the circle
              pygame.draw.circle(window, circle_color, circle_center, circle_radius)

   
    # Clear the window
    window.fill((0, 0, 0))  # Fill with black color

    pygame.display.update()

# Quit Pygame
pygame.quit()
