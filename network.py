import pygame

class Network():
    def __init__(self, screen, ratio, framerate, move, y_input) :
        self.latency = 33 * pow(10,-3)
        self.framerate = framerate
        self.ratio = ratio
        self.packets = []
        self.screen = screen
        self.color_packet = 'green'
        self.move = -move
        self.send_packet = []
        self.distance= screen.get_height()//2 - y_input

    def new_packet(self,packet):
        if packet != 0:
            self.packets.append(packet)
    
    def resend(self, packets) :
        for p in packets :
            self.send_packet.append(p)


    def actualise_income (self,server_buffer) :
        arrived_packet = []
        for p in self.packets:
            if p.y + p.height >= server_buffer.y :
                self.packets.remove(p)
                arrived_packet.append(p)
            else :
                p.x = p.x - self.move
                delta_y = (self.distance / self.framerate) *((1/self.framerate)/self.latency)
                p.y = p.y +  self.move *   delta_y
        return arrived_packet
    
    def actualise_outcome(self, client_y) :
        arrived_packet = []
        for p in self.send_packet :
            delta_x = - (self.latency * self.move)
            delta_y = p.y - client_y 
            if p.y <= client_y :
                self.send_packet.remove(p)
                arrived_packet.append(p)
            else :
                alpha = delta_y * self.move / delta_x
                p.x = p.x - self.move
                p.y = p.y - 1
        return arrived_packet


    def render(self):
        for p in self.packets :
            p.render(self.screen)
        for p in self.send_packet: 
            p.render(self.screen)