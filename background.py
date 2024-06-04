import pygame

class Background(): 
    def __init__(self, screen, ratio, speed):
        self.screen = screen
        self.move = -speed
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.background_color = "#ECF8F6"
        self.timestamp_color = pygame.Color("#226D68", alpha=20)
        self.timestamp = []
        self.pas = ratio
        self.size = 2
        self.id_timestamp = 0
        self.decalage = 20
        self.font = pygame.font.SysFont("comicsans", 20)
        for i in range(50, self.width, self.pas):
            rect = pygame.Rect(i, self.decalage, self.size, self.height )
            self.timestamp.append((rect, self.id_timestamp))
            self.id_timestamp += 1


    def render(self):
        self.screen.fill(self.background_color)
        for i in range (len(self.timestamp)) :
            rect = self.timestamp[i][0]
            pygame.draw.rect(self.screen, self.timestamp_color, rect, 40)
            text = self.font.render(str(self.timestamp[i][1]), 1, self.timestamp_color )
            x = rect.x - text.get_width()//2
            y = rect.y + 5 - self.decalage
            self.screen.blit(text, (x,y))

    def actualise(self):
        for time in self.timestamp :
            time[0].x = time[0].x + self.move

        if self.timestamp[0][0].x < 10 :
            self.timestamp.pop(0)

            new_rect = pygame.Rect(self.timestamp[-1][0].x + self.pas, self.decalage, self.size, self.height )
        
            self.timestamp.append((new_rect, self.id_timestamp))
            self.id_timestamp += 1
