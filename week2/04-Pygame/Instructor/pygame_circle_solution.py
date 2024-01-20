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

    #TODO Create your circle. The center of the circle is at 300,200.
    #The radius of the circle is 50 and the color of the circle is Green.
    
    # Define circle properties
    circle_color = (0, 255, 0)  # Green color
    circle_center = (300, 200)  # Center of the screen
    circle_radius = 50          # Radius of the circle
    
    # Draw the circle
    pygame.draw.circle(window, circle_color, circle_center, circle_radius)
    
    pygame.display.update()
