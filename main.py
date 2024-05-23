# Package import
import pygame
from background import Background
from client import Client

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

FRAMERATE = 60
speed = 2

fond = Background(screen, (speed * FRAMERATE) // FRAMERATE)
client = Client(1, 10, screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    fond.render()
    client.render()

    fond.actualise()


    dt = clock.tick(FRAMERATE) / 1000

pygame.quit()