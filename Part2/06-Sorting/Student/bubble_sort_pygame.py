import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
width = 800
height = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bubble Sort Visualization with Circles and Numbers")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Fonts
font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 48)

# Generate a list of random values
values_input = [9,8,7,6,3,4,2,1]
circle_radius = 20
num_values = len(values_input)
spacing = (width - 2 * circle_radius) // num_values

def draw_values(values, color_positions={}):
    screen.fill(white)
    for i, value in enumerate(values):
        color = red if i in color_positions else black
        pygame.draw.circle(screen, color, (i * spacing + circle_radius, height // 2), circle_radius)
        value_text = font.render(str(value), True, white)
        text_rect = value_text.get_rect(center=(i * spacing + circle_radius, height // 2))
        screen.blit(value_text, text_rect)
    pygame.display.update()

# TODO
# Call yield values, j, j+1 everytime when you try to swap the elements
def bubble_sort_step(values):

def is_sorted(values):
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def main():
    running = True
    clock = pygame.time.Clock()
    sort_gen = bubble_sort_step(values_input)
    sorting_done = False

    while running:
        clock.tick(1)  # Adjust the speed of visualization
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not sorting_done:
            try:
                values, pos1, pos2 = next(sort_gen)
                draw_values(values, color_positions={pos1: red, pos2: red})
            except StopIteration:
                sorting_done = True
                draw_values(values)
                if is_sorted(values):
                    message = "Sorting Successful!"
                    color = green
                else:
                    message = "Sorting Failed!"
                    color = red
                time.sleep(2)  # Delay to show the sorted result for 5 seconds

        # Keep the window open after sorting is done
        else:
            draw_values(values_input)
            if sorting_done:
                result_text = large_font.render(message, True, color)
                text_rect = result_text.get_rect(center=(width // 2, height // 4))
                screen.blit(result_text, text_rect)
                pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
