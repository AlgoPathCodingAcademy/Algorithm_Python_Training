import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Collision Detection with Color Change and Movement")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, color, radius, position):
        super().__init__()
        self.radius = radius
        self.position = list(position)  # Convert to list for mutability
        self.color = color
        self.update_image()

    def update_image(self):
        self.image = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=self.position)

    def change_color(self, color):
        self.color = color
        self.update_image()

    def move(self, dx, dy):
        # Update position and rect for movement
        self.position[0] += dx
        self.position[1] += dy
        self.rect.x += dx
        self.rect.y += dy

# Create circle sprites
moving_circle = CircleSprite(GREEN, 30, (200, 240))
static_circle = CircleSprite(GREEN, 30, (400, 240))

# Sprite group for drawing
all_sprites = pygame.sprite.Group([moving_circle, static_circle])

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move the moving circle with arrow keys
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_UP]:
            dy -= 5
        if keys[pygame.K_DOWN]:
            dy += 5
            
        moving_circle.move(dx, dy)

    # Check for collision and change color accordingly
    if pygame.sprite.collide_circle(moving_circle, static_circle):
        moving_circle.change_color(RED)
    else:
        moving_circle.change_color(GREEN)

    # Draw sprites
    all_sprites.draw(screen)

    pygame.display.update()
