import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()
window  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Demo")


running = True
while running:

    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
              #The center of the circle is at 300,200.
              #The radius of the circle is 50 and the color of the circle is Green.
              
              # Define circle properties
              circle_color = (0, 255, 0)  # Green color
              circle_center = (300, 200)  # Center of the screen
              circle_radius = 50          # Radius of the circle
              
              # Draw the circle
              pygame.draw.circle(window, circle_color, circle_center, circle_radius)
            elif event.key == pygame.K_l:
              #The start of the line is at 100,100.
              #The end of the line is at 500, 300.
              #The color of the line is Blue.
              #The width of the line is 5
              line_color = (0, 255, 0)  # Green color
              start_pos = (100, 100)    # Starting position of the line
              end_pos = (500, 300)      # Ending position of the line
              line_width = 5            # Width of the line
              
              # Draw the line
              pygame.draw.line(window, line_color, start_pos, end_pos, line_width)
    
    pygame.display.update()

