import random, sys, copy, os, pygame
from pygame.locals import *

pygame.init()
window  = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Demo")

#TODO Create your font(text) with default font size and its surface
# You could choose your font size if it is too small or too big
# The text is "Hello, Pygame!". The color of the text is white

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Clear the window
    window.fill((0, 0, 0))  # Fill with black color

    #TODO Blit the font(text) to the window(primary surface)
    #The text should be in position x = 50, y = 50
    
    pygame.display.update()
