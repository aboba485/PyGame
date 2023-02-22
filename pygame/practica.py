import pygame
import sys
import random

WIDTH = 480
HEIGHT = 600

class Bird:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 0

    def update(self):
        self.y += self.velocity
        self.velocity += 1.5
        self.y = min(HEIGHT - self.height, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Pipe:
    def __init__(self, x, height, width, color):
        self.x = x
        self.height = height
        self.width = width
        self.color = color

    def update(self):
        self.x -= 2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.x, HEIGHT-self.height, self.width, self.height))

def check_collision(bird, pipes):
    bird_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)

    for pipe in pipes:
        pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.height)
        if bird_rect.colliderect(pipe_rect):
            return True

        pipe_rect = pygame.Rect(pipe.x, HEIGHT - pipe.height, pipe.width, pipe.height)
        if bird_rect.colliderect(pipe_rect):
            return True

    return False

def game_over(screen, font):
    text = font.render("Game Over!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    bird = Bird(100, 300, 20, 20, (255, 255, 255))
    pipes = [Pipe(600, random.randint(200, 400), 40, (255, 255, 255))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.velocity = -10

        bird.update()
