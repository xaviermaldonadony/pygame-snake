import pygame
from pygame.locals import *


def draw_screen():
    screen.fill(bg)


pygame.init()

# Create blank game windows
screen_width = 600
screen_height = 600

# Create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

# Define game variables
cell_size = 10

# Create snake
# Set it in the middle of the screen
snake_pos = [[int(screen_width / 2), int(screen_height / 2) ]]

snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 3])

# Define colors
bg = (255, 200, 150)
# green
body_inner = (50, 175, 25)
# purple
body_outer = (100, 100, 200)
red = (255, 0, 0)


# Setup oop with an exit flag
run = True

while run:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Draw snake
    head = 1
    for cor in snake_pos:
        if head == 0:
            # x,y coordinate, width, height
            pygame.draw.rect(screen, body_outer, (cor[0], cor[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (cor[0] + 1, cor[1] + 1, cell_size - 2, cell_size -2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (cor[0], cor[1], cell_size, cell_size))
            pygame.draw.rect(screen, red, (cor[0] + 1, cor[1] + 1, cell_size - 2, cell_size -2))
            head = 0

        # Update the display
    pygame.display.update()

# End pygame
pygame.quit()

# Create a snake an set up the snake list
