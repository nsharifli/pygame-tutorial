# Pygame template file
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

running = True

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (Events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update

    # draw / render
    screen.fill(BLACK)

    # after drawing everything flip the display
    pygame.display.flip()

pygame.quit()
