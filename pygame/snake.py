import pygame
import time
import random as rand

# Initialize pygame
pygame.init()

# Set the width and height of the screen (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create a 2D array for the snake's body
snake_list = [[100, 50], [90, 50], [80, 50]]

# Initialize the snake's starting position and its size
snake_rect = pygame.Rect(100, 50, 10, 10)

# Create a 2D array for the apple's starting position
apple_pos = [300, 200]

# Initialize the apple's starting position and its size
apple_rect = pygame.Rect(300, 200, 10, 10)

# Define the colors that will be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Initialize the snake's starting direction
direction = 'right'

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Move the snake based on the direction
    if direction == 'w':
        snake_rect.x += 10
    if direction == 'a':
        snake_rect.x -= 10
    if direction == 's':
        snake_rect.y -= 10
    if direction == 'd':
        snake_rect.y += 10

    # Check if the snake's head has collided with the apple
    if snake_rect.colliderect(apple_rect):
        # If so, move the apple to a new random location
        apple_rect.x = 20 + (10 * int(30 * rand()))
        apple_rect.y = 20 + (10 * int(20 * rand()))

    # Move the rest of the snake
    for i in range(len(snake_list) - 1, 0, -1):
        snake_list[i] = (snake_list[i - 1][0], snake_list[i - 1][1])

    # Update the snake's head position
    snake_list[0] = [snake_rect.x, snake_rect.y]

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(black)

    # Draw the snake
    for pos in snake_list:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the apple
    pygame.draw.rect(screen, red, apple_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick

    #kjbef io kjw 