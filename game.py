import pygame
from bloc import Bloc

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = "black"
        # Constant
        self.BLOC_SIZE = self.screen.get_width()/4

        # Blocs
        self.bloc = Bloc(self, 0, 0, 2)
        self.blocs = pygame.sprite.Group()
        self.font_bloc = pygame.font.SysFont("Arial", 40)




    def set_font_position(self, rect, value, font):
        font_size = font.size(str(value))
        x = rect.x + rect.width/2 - font_size[0]/2
        y = rect.y + rect.height/2 - font_size[1]/2
        return (x, y)

    def get_2_power(self, num):
        i = 0
        while True:
            num = num/2
            i += 1
            if num == 1:
                power = i
                break
        return power

    def set_color(self, value):
        pow = self.get_2_power(value)
        R = 255 - 10*pow
        G = 255 - 25*pow
        B = 255 - 35*pow
        if G < 0:
            G = 0
        if B < 0:
            B = 0
        return (R, G, B)

    def update(self):
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen, self.set_color(self.bloc.value), (self.bloc.rect.x, self.bloc.rect.y, self.bloc.rect.width, self.bloc.rect.height))
        self.screen.blit(self.font_bloc.render(str(self.bloc.value), True, (0, 0, 0)),
                         self.set_font_position(self.bloc.rect, self.bloc.value, self.font_bloc))

