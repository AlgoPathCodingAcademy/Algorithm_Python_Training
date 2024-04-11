import pygame
import random

#Please use yield to return the current index being checked
def linear_search(arr, x):
#TODO

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linear Search Visualization")

# Array and target value
numbers = random.sample(range(1, 101), 10)
target = random.choice(numbers)

# Linear search generator
search_process = linear_search(numbers, target)

# Fonts
font = pygame.font.Font(None, 36)

running = True
current_index = None
advance_search = False
search_completed = False
search_result = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Press any key to advance the linear search
            advance_search = True

    screen.fill((255, 255, 255))  # Clear screen

    # Display the target number
    target_text = font.render(f"Target Number: {target}", True, (0, 128, 0))  # Green color for target number
    screen.blit(target_text, (10, 10))  # Position at the top-left corner

    # Draw numbers and highlight the current index being checked
    for i, number in enumerate(numbers):
        color = (0, 0, 0)  # Default color (black)
        if i == current_index:
            color = (255, 0, 0)  # Highlight current index (red)

        # Render the number
        num_text = font.render(str(number), True, color)
        screen.blit(num_text, (i * (WIDTH // len(numbers)), HEIGHT // 2))

        # Render the index below the number
        index_text = font.render(str(i), True, (0, 0, 255))  # Blue color for index
        screen.blit(index_text, (i * (WIDTH // len(numbers)), HEIGHT // 2 + 30))

    # Perform one step of linear search if a key was pressed
    if advance_search and not search_completed:
        try:
            current_index = next(search_process)
        except StopIteration as e:
            search_completed = True
            search_result = e.value
        advance_search = False

    if search_completed:
        result_text = font.render(f"Found at index: {search_result}" if search_result != -1 else "Not Found", True, (0, 0, 128))
        screen.blit(result_text, (50, 50))

    pygame.display.flip()  # Update screen

pygame.quit()
