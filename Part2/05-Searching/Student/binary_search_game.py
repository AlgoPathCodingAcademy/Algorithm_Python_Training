import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Search Visualization")

#yield low, high, mid  # Current state of search
def binary_search(arr, x):
#TODO

# Sorted array and target value
numbers = sorted(random.sample(range(1, 101), 10))
target = random.choice(numbers)

# Binary search generator
search_process = binary_search(numbers, target)

# Fonts
font = pygame.font.Font(None, 36)

running = True
search_step = None

running = True
search_step = None
advance_search = False
search_completed = False
search_result = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Press any key to advance the binary search
            advance_search = True

    screen.fill((255, 255, 255))  # Clear screen


    # Display the target number
    target_text = font.render(f"Target Number: {target}", True, (0, 128, 0))  # Green color for target number 
    screen.blit(target_text, (10, 10))  # Position at the top-left corner

    # Draw numbers and their indices, and highlight the search area
    for i, number in enumerate(numbers):
        # ... (same as before)
        color = (0, 0, 0)  # Default color (black)
        if search_step:
            low, high, mid = search_step
            if low <= i <= high:
                color = (255, 0, 0)  # Highlight search area (red)
                if i == mid:
                    color = (0, 255, 0)  # Highlight middle element (green)

        # Render the number
        num_text = font.render(str(number), True, color)
        screen.blit(num_text, (i * (WIDTH // len(numbers)), HEIGHT // 2))

        # Render the index below the number
        index_text = font.render(str(i), True, (0, 0, 255))  # Blue color for index
        screen.blit(index_text, (i * (WIDTH // len(numbers)), HEIGHT // 2 + 30))

    # Perform one step of binary search if a key was pressed
    if advance_search:
        try:
            search_step = next(search_process)
        except StopIteration as e:
            search_completed = True
            search_result = e.value

        advance_search = False

    if search_completed:
        if search_result == None:
            break
        # Render the result text
        result_text = font.render(f"IsFound: {search_result}", True, (0, 0, 128))
        screen.blit(result_text, (50, 50))

    pygame.display.flip()  # Update screen

pygame.quit()
