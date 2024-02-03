import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Object Without Clearing")

# Object properties
obj_color = (0, 255, 0)  # Green
obj_pos = [300, 200]  # Initial position
obj_radius = 20
speed = [2, 2]  # Movement speed [x, y]

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop flag
running = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:  # Press ESC to quit
                running = False
                
    #window.fill((0, 0, 0))

    # Update object position
    obj_pos[0] += speed[0]
    obj_pos[1] += speed[1]

    # Bounce off the edges
    if obj_pos[0] + obj_radius > 600 or obj_pos[0] - obj_radius < 0:
        speed[0] = -speed[0]
    if obj_pos[1] + obj_radius > 400 or obj_pos[1] - obj_radius < 0:
        speed[1] = -speed[1]

    # Draw the object at its new position
    pygame.draw.circle(window, obj_color, obj_pos, obj_radius)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
