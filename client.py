import pygame

class Client():
    def __init__(self, id, init_frame, screen) :
        self.id = id
        self.screen = screen
        self.frame = init_frame
        self.color = pygame.Color("#18534F", alpha=20)
        self.height = 45
        self.width = self.screen.get_width() // (4/3) 
        self.x = 10
        self.y = 40

    def render(self) :
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rect, 40)

