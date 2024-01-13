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
   
    # Clear the window
    window.fill((0, 0, 0))  # Fill with black color

    # Draw a rectangle directly on the main surface
    rect_color = (255, 0, 0)  # Red color
    rect_x, rect_y = 100, 100  # Position of the rectangle
    rect_width, rect_height = 200, 100  # Size of the rectangle
    
    pygame.draw.rect(window, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
