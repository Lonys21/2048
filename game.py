import pygame
from bloc import Bloc

class Game:
    def __init__(self, screen):
        self.screen = screen
        # Background
        self.background = pygame.image.load("assets/grid.png")
        self.background = pygame.transform.scale(self.background, (800, 800))
        self.background_color = "darkgray"

        # Constant
        self.platform = 15
        self.TOP_SIZE = 200
        self.BLOC_SIZE = (self.screen.get_width() - 16*5)/4 + 1

        # Blocs
        self.bloc = Bloc(self, 16, 216, 2)
        self.blocs = pygame.sprite.Group()
        self.blocs.add(self.bloc)
        self.font_bloc = pygame.font.SysFont("Arial", 40)

        # Grid
        # [[value, (x,y)]]
        self.grid = [[[0, (self.platform, self.platform + self.TOP_SIZE)], [16, (self.platform*2 + self.BLOC_SIZE, self.platform + self.TOP_SIZE)],
                      [1024, (self.platform*3 + self.BLOC_SIZE*2, self.platform + self.TOP_SIZE)], [2, (self.platform*4+self.BLOC_SIZE*3, self.platform + self.TOP_SIZE)]],

                     [[2, (self.platform, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)], [4, (self.platform * 2 + self.BLOC_SIZE, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)],
                      [2, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)], [16, (self.platform * 4 +self.BLOC_SIZE*3, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)]],

                     [[2, (self.platform, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)], [0, (self.platform * 2 + self.BLOC_SIZE, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)],
                      [0, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)], [2, (self.platform * 4+self.BLOC_SIZE*3, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)]],

                    [[4, (self.platform, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)], [16, (self.platform * 2 + self.BLOC_SIZE, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)],
                     [2, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)], [16, (self.platform * 4+self.BLOC_SIZE*3, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)]]]

    def update_grid_left(self):
        for i in self.grid:
            i_ = i[::]
            for n in range(len(i)):
                if not n == 0:
                    a = 1
                    b = 0
                    while i[(n-b)-a][0] == 0 and n-b > 0:
                        i[(n-b)-a][0] = i[n-b][0]
                        i[n-b][0] = 0
                        b += 1
                    if i[n-b][0] == i[n-b-1][0] and i[n-b-1][0] == i_[n-b-1][0] and n - b > 0:
                        i[n-b-1][0] = i[n-b][0]*2
                        i[n-b][0] = 0

    def update_grid_right(self):
        k = 0
        for i in self.grid:
            i = i[::-1]
            i_ = i[::]
            for n in range(len(i)):
                if not n == 0:
                    a = 1
                    b = 0
                    while i[(n - b) - a][0] == 0 and n - b > 0:
                        i[(n - b) - a][0] = i[n - b][0]
                        i[n - b][0] = 0
                        b += 1
                    if i[n - b][0] == i[n - b - 1][0] and i[n - b - a][0] == i_[n - b - 1][0] and n - b > 0:
                        i[n - b - 1][0] = i[n - b][0] * 2
                        i[n - b][0] = 0
            self.grid[k] = i[::-1]
            k += 1

    def update_block_grid(self):
        for row in self.grid:
            for bloc in row:
                if not bloc[0] == 0:
                    pygame.draw.rect(self.screen, self.set_color(bloc[0]), (bloc[1][0], bloc[1][1], self.BLOC_SIZE, self.BLOC_SIZE))
                    self.screen.blit(self.font_bloc.render(str(bloc[0]), True, (0, 0, 0)),
                                     self.set_font_position(bloc[1][0], bloc[1][1], bloc[0], self.font_bloc))

    def set_font_position(self, x, y, value, font):
        font_size = font.size(str(value))
        x_ = x + self.BLOC_SIZE/2 - font_size[0]/2
        y_ = y + self.BLOC_SIZE/2 - font_size[1]/2
        return (x_, y_)

    def get_2_power(self, num):
        i = 0
        if num == 0:
            return 0
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
        self.update_block_grid()

