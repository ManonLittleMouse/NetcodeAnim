import pygame
from packet import Packet

Y_DECAL = 60
Y_IMPUT_DECAL = 10
CLIENT_COLOR = "#18534F"
class Client():
    def __init__(self, id, init_frame, screen, HEIGHT, speed) :
        self.id = id
        self.screen = screen
        self.frame = init_frame
        self.move = - speed
        self.color = pygame.Color(CLIENT_COLOR, alpha=20)
        self.height = HEIGHT
        self.width = self.screen.get_width() // (4/3)
        self.x = 10
        self.y = 0 
        self.y_input = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        if id == 1 :
            self.y = Y_DECAL
            self.y_input = self.y + self.height + Y_IMPUT_DECAL
        
        if id == 2 :
            self.y = screen.get_height() - Y_DECAL
            self.y_input = self.y - Y_IMPUT_DECAL

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.font_size = 30
        self.font = pygame.font.SysFont("comicsans", self.font_size)
        self.text =  self.font.render("Client " + str(self.id), 1, self.color )
        self.networks = []



    def render(self) :
        pygame.draw.rect(self.screen, self.color, self.rect, 40)
        self.screen.blit(self.text, (self.x + self.font_size//2, self.y + self.height + self.font_size//2))
        for p in self.networks: 
            p.render(self.screen)

    def new_frame(self, timestamps):
        for time in timestamps :
            t = time[1]
            rect = time[0]
            if self.rect.colliderect(rect) and t > self.frame :
                self.frame = t
                p = Packet('oui', rect.x, self.y_input, t, color = self.color)
                self.networks.append(p)
                p_send = Packet('oui', rect.x, self.y_input, t, color = 'green')
                return p_send
        return 0
    
    def update_network(self) :
        for p in self.networks: 
            if p. x <= self.x :
                self.networks.remove(p)
            else: 
                p.x = p.x - self.move

    def rollback(self, packets) :
        for p_ in packets :
            for p in self.networks :
                if p_.frame == p.frame  :
                    if p_.msg == p.msg :
                        p.color = 'green'
                    else :
                        p.color = 'red'
