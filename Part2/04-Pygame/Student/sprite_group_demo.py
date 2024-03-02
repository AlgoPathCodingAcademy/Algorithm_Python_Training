import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Shooting Example")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10  # Speed; negative moves it upwards

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it goes off-screen

# Group for all sprites for easy updates and rendering
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()  # Specific group for bullets

def shoot_bullet(x, y):
    bullet = Bullet(x, y)
    all_sprites.add(bullet)
    bullets.add(bullet)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot a bullet from the middle, bottom of the screen
                    shoot_bullet(WIDTH // 2, HEIGHT - 20)

        # Update
        all_sprites.update()

        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()  # After drawing everything, flip the display
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
