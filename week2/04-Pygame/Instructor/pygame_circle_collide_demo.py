import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Circle details
circle_radius = 20
circle_x = screen_width // 4
circle_y = screen_height // 4
circle_speed = 0.1

# Target circle details
target_x = screen_width * 3 // 4
target_y = screen_height // 2

# Game clock
#clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses to move the circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed

    # Fill the screen with black
    screen.fill(black)

    # Draw the circles
    pygame.draw.circle(screen, white, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(screen, red, (target_x, target_y), circle_radius)

    # Check for collision
    distance = ((circle_x - target_x) ** 2 + (circle_y - target_y) ** 2) ** 0.5
    if distance < circle_radius * 2:
        font = pygame.font.Font(None, 74)
        text = font.render("Collide", 1, white)
        screen.blit(text, (screen_width // 2 - 100, screen_height // 2 - 50))
        #pygame.display.flip()  # Update the full display Surface to the screen
        #pygame.time.wait(2000)  # Wait for 2 seconds to show the collide text
        #running = False

    # Update the screen
    pygame.display.update()

    # Cap the frame rate
    #clock.tick(60)

pygame.quit()

