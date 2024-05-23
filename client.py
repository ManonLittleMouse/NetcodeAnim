import pygame

class Client():
    def __init__(self, id, init_frame, screen, HEIGHT) :
        self.id = id
        self.screen = screen
        self.frame = init_frame
        self.color = pygame.Color("#18534F", alpha=20)
        self.height = HEIGHT
        self.width = self.screen.get_width() // (4/3) 
        self.x = 10
        self.y = 60
        self.y_input = self.y + self.height + 10
        self.font_size = 30
        self.font = pygame.font.SysFont("comicsans", self.font_size)
        self.text =  self.font.render("Client", 1, self.color )
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.networks = []



    def render(self, timestamps) :
        pygame.draw.rect(self.screen, self.color, self.rect, 40)
        self.screen.blit(self.text, (self.x + self.font_size//2, self.y + self.height + self.font_size))
        for time in timestamps :
            rect = time[0]
            t = time[1]
            if t <= self.frame : 
                pos_input = pygame.Rect(rect.x,self.y_input , 10, 10)
                pygame.draw.rect(self.screen, self.color , pos_input ,40 )


    def new_frame(self, timestamps):
        for time in timestamps :
            t = time[1]
            rect = time[0]
            if self.rect.colliderect(rect) and t > self.frame :
                self.frame = t
                self.networks.append((t,self.y_input ))

    def update_network(self, server) :
        for n in self.networks: 
            if n[1] <= server.y + server.height//2 and n[0] < server.frame  :
                self.networks.remove(n)
            else: 
                n = (n[0], n[1] + 1)