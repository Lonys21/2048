import pygame
from bloc import Bloc

class Game:
    def __init__(self, screen):
        self.screen = screen
        # Background
        self.background = pygame.image.load("assets/grid.png")
        self.background_color = "black"

        # Constant
        self.PLATFORM_SIZE = 16
        self.BLOC_SIZE = (self.screen.get_width() - 16*5)/4

        # Blocs
        self.bloc = Bloc(self, 16, 216, 2)
        self.blocs = pygame.sprite.Group()
        self.blocs.add(self.bloc)
        self.font_bloc = pygame.font.SysFont("Arial", 40)

        # Grid
        self.grid = [[2, 2, 2, 4],
                     [2, 2, 2, 2],
                     [2, 4, 2, 2],
                     [4, 2, 2, 4]]

    def update_grid(self, direction):
        if direction == 'left':
            for i in self.grid[::]:
                i_ = i[::]
                for n in range(len(i)):
                    if not n == 0:
                        a = 1
                        b = 0
                        while i[(n-b)-a] == 0 and n-b > 0:
                            print(i, n, i[n-b])
                            i[(n-b)-a] = i[n-b]
                            i[n-b] = 0
                            b += 1
                        if i[n-b] == i[n-b-1] and i[n-b-1] == i_[n-b-1]:
                            i[n-b-1] = i[n-b]*2
                            i[n-b] = 0
        return





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
        self.screen.blit(self.background, (0, 200))
        for bloc in self.blocs:
            pygame.draw.rect(self.screen, self.set_color(bloc.value), (bloc.rect.x, bloc.rect.y, bloc.rect.width, bloc.rect.height))
            self.screen.blit(self.font_bloc.render(str(bloc.value), True, (0, 0, 0)),
                             self.set_font_position(bloc.rect, bloc.value, self.font_bloc))

