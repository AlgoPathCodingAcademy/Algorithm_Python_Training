import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rectangle Collision Example with Sprites')

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Movement speed
speed = 5

# Sprite classes
class MovingRect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect(topleft=(300, 300))
        self.speed = speed

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class StaticRect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect(topleft=(400, 400))

# Create sprite groups
all_sprites = pygame.sprite.Group()
moving_rect = MovingRect()
static_rect = StaticRect()

# Add sprites to the group
all_sprites.add(moving_rect)
all_sprites.add(static_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        moving_rect.update(keys)

    # Collision check
    if pygame.sprite.collide_rect(moving_rect, static_rect):
        moving_rect.image.fill(red)
    else:
        moving_rect.image.fill(green)

    # Drawing
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
