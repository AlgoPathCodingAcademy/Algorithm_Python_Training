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
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        self.speed = 5

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep the player within the screen bounds
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)  # Add bullet only to bullets group

# Groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()  # Separate group for bullets

# Create a player instance and add it to the all_sprites group
player = Player()
all_sprites.add(player)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Update
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)  # Update player with pressed keys directly
        bullets.update()  # Update bullets independently

        # Draw / render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        bullets.draw(screen)  # Draw bullets independently

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

