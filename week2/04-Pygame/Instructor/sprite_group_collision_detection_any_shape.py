import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Polygon Collision Example")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS
FPS = 30
clock = pygame.time.Clock()

# Polygon class
class Polygon(pygame.sprite.Sprite):
    def __init__(self, points, color, position=(0,0)):
        super().__init__()
        self.original_points = points
        self.color = color
        self.image = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.position = position
        self.update_polygon()
        self.mask = pygame.mask.from_surface(self.image)

    def update_polygon(self):
        self.image.fill((0,0,0,0))  # Clear the surface by filling it with a fully transparent color
        pygame.draw.polygon(self.image, self.color, self.original_points)
        self.mask = pygame.mask.from_surface(self.image)  # Update mask for collision detection

    def move(self, dx, dy):
        # Move the polygon by updating its position
        self.position = (self.position[0] + dx, self.position[1] + dy)
        moved_points = [(x + dx, y + dy) for x, y in self.original_points]
        self.original_points = moved_points
        self.update_polygon()

def check_collision(polygon1, polygon2):
    offset_x = polygon2.position[0] - polygon1.position[0]
    offset_y = polygon2.position[1] - polygon1.position[1]
    return polygon1.mask.overlap(polygon2.mask, (offset_x, offset_y)) is not None

# Define polygons
moving_polygon = Polygon([(0, 0), (50, 0), (25, 50)], GREEN, position=(300, 300))
static_polygon = Polygon([(0, 0), (50, 0), (25, 50)], GREEN, position=(400, 400))

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -3
    if keys[pygame.K_RIGHT]:
        dx = 3
    if keys[pygame.K_UP]:
        dy = -3
    if keys[pygame.K_DOWN]:
        dy = 3
    moving_polygon.move(dx, dy)

    # Check for collision and change color accordingly
    if check_collision(moving_polygon, static_polygon):
        moving_polygon.color = RED
    else:
        moving_polygon.color = GREEN
    moving_polygon.update_polygon()

    # Draw polygons
    screen.blit(moving_polygon.image, moving_polygon.position)
    screen.blit(static_polygon.image, static_polygon.position)

    pygame.display.flip()
    clock.tick(FPS)
