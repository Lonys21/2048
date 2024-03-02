import pygame
from bloc import Bloc

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bloc = Bloc(self)
        self.font_bloc = pygame.font.SysFont("Arial", 20)

    def set_font_position(self, rect, value, font):
        font_size = font.size(str(value))
        x = rect.x + rect.width/2 - font_size[0]/2
        y = rect.y + rect.height/2 - font_size[1]/2
        return (x, y)

    def update(self):
        self.screen.fill("white")
        pygame.draw.rect(self.screen, (0, 0, 0), (self.bloc.rect.x, self.bloc.rect.y, self.bloc.rect.width, self.bloc.rect.height))
        self.screen.blit(self.font_bloc.render(str(self.bloc.value), True, (100, 100, 100)),
                         self.set_font_position(self.bloc.rect, self.bloc.value, self.font_bloc))

