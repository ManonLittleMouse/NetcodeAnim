# Package import
import pygame
from background import Background
from client import Client
from server import Server

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

FRAMERATE = 60
HEIGHT = 25
speed = 1

fond = Background(screen, (speed * FRAMERATE) // FRAMERATE)
client = Client(1, 10, screen, HEIGHT)
server = Server(screen, HEIGHT, fond)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    fond.render()
    client.render(fond.timestamp)
    server.render()

    client.new_frame(fond.timestamp)
    fond.actualise()


    dt = clock.tick(FRAMERATE) / 1000

pygame.quit()