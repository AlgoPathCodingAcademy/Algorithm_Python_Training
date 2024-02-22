# Only for showing the usage of sprite and its member function collide_circle
# The circle won't collide because there is no movement code inside

import pygame
import sys

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 300))

class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, color, radius, position):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=position)
        self.radius = radius

# Set up sprites
sprite1 = CircleSprite((255, 0, 0), 20, (100, 150))
sprite2 = CircleSprite((0, 0, 255), 20, (300, 150))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for collision
    if pygame.sprite.collide_circle(sprite1, sprite2):
        print("Collision detected!")

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(sprite1.image, sprite1.rect)
    screen.blit(sprite2.image, sprite2.rect)
    pygame.display.flip()

    pygame.time.delay(100)
