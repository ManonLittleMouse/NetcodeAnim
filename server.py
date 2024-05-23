import pygame

class Server:
    def __init__(self, screen, HEIGHT, background): 
        self.screen = screen
        self.x = 10
        self.y = self.screen.get_height()//2
        self.height = HEIGHT
        self.width = self.screen.get_width()//2
        self.color = pygame.Color("#FEEAA1", alpha=20)
        self.font_size = 30
        self.font = pygame.font.SysFont("comicsans", self.font_size)
        self.text =  self.font.render("Server", 1, self.color )
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buffer_length = 2
        self.buffer_size = self.buffer_length * background.pas
        self.buffer_render = pygame.Rect(self.x + self.width, self.y + self.height//2 , self.buffer_size, 2 )

    def render(self) :
        pygame.draw.rect(self.screen, self.color, self.rect, 40)
        self.screen.blit(self.text, (self.x + self.font_size//2, self.y + self.height + self.font_size//3))
        pygame.draw.rect(self.screen, 'black', self.buffer_render, 40)