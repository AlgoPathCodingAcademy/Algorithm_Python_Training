import random, sys, copy, os, pygame, math
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

    #TODO Create your arc and draw it. 
    # Blue color
    # Bounding rectangle for the arc - (100,100,200,200)
    # Start angle (in radians) - 0 degree
    # End angle (in radians)- 180 degree
    # Width of the arc line - 5
    arc_color = (0, 0, 255)  # Blue color
    arc_rect = pygame.Rect(100, 100, 200, 200)
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    arc_width = 5
    
    # Draw the arc
    pygame.draw.arc(window, arc_color, arc_rect, start_angle, end_angle, arc_width)
    
    pygame.display.update()
