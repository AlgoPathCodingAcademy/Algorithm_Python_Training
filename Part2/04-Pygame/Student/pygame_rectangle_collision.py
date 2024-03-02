import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rectangle Collision Example')

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Rectangles (x, y, width, height)
moving_rect = pygame.Rect(300, 300, 50, 50)
static_rect = pygame.Rect(400, 400, 50, 50)

# Movement speed
speed = 5

# Function to check collision
def check_collision(rect1, rect2):
    # TODO: Implement the collision detection logic
    isCollide = False
    
    return isCollide

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          keys = pygame.key.get_pressed()
          if keys[pygame.K_LEFT]:
              moving_rect.x -= speed
          if keys[pygame.K_RIGHT]:
              moving_rect.x += speed
          if keys[pygame.K_UP]:
              moving_rect.y -= speed
          if keys[pygame.K_DOWN]:
              moving_rect.y += speed

    # Check for collision
    if check_collision(moving_rect, static_rect):
        collision_color = red
    else:
        collision_color = green

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, collision_color, moving_rect)
    pygame.draw.rect(screen, green, static_rect)
    pygame.display.flip()

pygame.quit()
