# Package import
import pygame
from background import Background
from client import Client
from server import Server
from network import Network

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

FRAMERATE = 60
HEIGHT = 25
PXL_TIME_RATIO = 75
speed = 1

fond = Background(screen, PXL_TIME_RATIO,  (speed * FRAMERATE) // FRAMERATE)
client1 = Client(1, 10, screen, HEIGHT, fond.move)
client2= Client(2, 10, screen, HEIGHT, fond.move)

server = Server(screen, HEIGHT, fond)
network = Network(screen, PXL_TIME_RATIO, FRAMERATE, fond.move, client1.y_input)
while running:




    # Render each component 
    fond.render()
    client1.render()
    client2.render()
    server.render()
    network.render()


    # Actualise each component for next frame
    network.new_packet(client1.new_frame(fond.timestamp))
    network.new_packet(client2.new_frame(fond.timestamp))

    fond.actualise()
    client1.update_network()
    server.buffer_arrived(network.actualise_income(server.buffer_render))
    client1.rollback(network.actualise_outcome(client1.y_input))
    network.resend(server.actualise())



    # Check incoming event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("down")
                server.buffer_length += 1
            if event.key == pygame.K_UP :
                print("up")
                server.buffer_length -= 1

    pygame.display.flip()

    
    dt = clock.tick(FRAMERATE) / 1000



pygame.quit()