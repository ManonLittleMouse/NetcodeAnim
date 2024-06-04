import pygame

class Server:
    def __init__(self, screen, HEIGHT, background): 
        self.screen = screen
        self.frame = 0
        self.move = background.move
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
        self.pas = background.pas
        self.buffer_size = self.buffer_length * self.pas
        self.buffer_render = pygame.Rect(self.x + self.width, self.y + self.height//2 , self.buffer_size, 2 )
        self.buffer = []

    def render(self) :
        pygame.draw.rect(self.screen, self.color, self.rect, 40)
        self.screen.blit(self.text, (self.x + self.font_size//2, self.y + self.height + self.font_size//3))
        pygame.draw.rect(self.screen, 'black', self.buffer_render, 40)
        for p in self.buffer :
            p.render(self.screen)

    def buffer_arrived(self, buff) :
        for p in buff :
            self.buffer.append(p)

    def actualise(self):
        send_packet = []
        for p in self.buffer:
            if p.x < self.buffer_render.x :
                self.buffer.remove(p)
                send_packet.append(p)
            else :
                p.x = p.x + self.move
        return send_packet