import pygame

class Packet():
    def __init__(self, msg, x,y, t, width = 10, height = 10, color = 'green'):
        self.x = x
        self.y = y
        self.msg = msg
        self.width = width
        self.height = height
        self.color = color
        self.frame = t

    def render(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height )
        pygame.draw.rect(screen, self.color, rect , 40)
