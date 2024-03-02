pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Demo")

# Initialize the flag
circle_drawn = False

running = True
while running:
    # Clear the window at the start of each loop iteration
    window.fill((0, 0, 0))  # Fill with black color
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # If 'S' key is pressed, set the flag
                circle_drawn = True

    # Draw the circle based on the flag
    if circle_drawn:
        circle_color = (0, 255, 0)  # Green color
        circle_center = (300, 200)  # Center of the screen
        circle_radius = 50          # Radius of the circle
        pygame.draw.circle(window, circle_color, circle_center, circle_radius)

    pygame.display.update()

pygame.quit()
