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
    
    pygame.display.update()
