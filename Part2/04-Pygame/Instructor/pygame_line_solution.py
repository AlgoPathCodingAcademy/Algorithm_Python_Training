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

    #TODO Create your line and draw it. 
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
