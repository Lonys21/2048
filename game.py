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
        self.platform = 16
        self.TOP_SIZE = 200
        self.BLOC_SIZE = (self.screen.get_width() - 16*5)/4

        # Blocs
        self.direction = ''
        self.bloc = Bloc(self, self.platform, 216, 2, 0)
        self.bloc2 = Bloc(self, self.platform, 412, 2, 1)
        self.bloc3 = Bloc(self, self.platform, 608, 4, 2)
        self.bloc4 = Bloc(self, self.platform*2 + self.BLOC_SIZE, self.TOP_SIZE + self.platform, 2, 3)
        self.bloc5 = Bloc(self, self.platform*3 + self.BLOC_SIZE*2, self.TOP_SIZE + self.platform, 2, 4)
        self.bloc6 = Bloc(self, self.platform*4 + self.BLOC_SIZE*3, self.TOP_SIZE + self.platform, 2, 5)
        self.blocs = pygame.sprite.Group()
        self.blocs.add(self.bloc, self.bloc2, self.bloc3, self.bloc4, self.bloc5, self.bloc6)
        self.font_bloc = pygame.font.SysFont("Arial", 40)
        self.blocs_coos = []

        # Grid
        # [[value, (x,y)]]
        """self.grid = [[[2, (self.platform, self.platform + self.TOP_SIZE)], [0, (self.platform*2 + self.BLOC_SIZE, self.platform + self.TOP_SIZE)],
                      [0, (self.platform*3 + self.BLOC_SIZE*2, self.platform + self.TOP_SIZE)], [2, (self.platform*4+self.BLOC_SIZE*3, self.platform + self.TOP_SIZE)]],

                     [[2, (self.platform, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)], [0, (self.platform * 2 + self.BLOC_SIZE, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)],
                      [0, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)], [0, (self.platform * 4 +self.BLOC_SIZE*3, self.platform*2 + self.BLOC_SIZE + self.TOP_SIZE)]],

                     [[2, (self.platform, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)], [0, (self.platform * 2 + self.BLOC_SIZE, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)],
                      [4, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)], [0, (self.platform * 4+self.BLOC_SIZE*3, self.platform*3 + self.BLOC_SIZE*2 + self.TOP_SIZE)]],

                    [[2, (self.platform, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)], [2, (self.platform * 2 + self.BLOC_SIZE, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)],
                     [2, (self.platform * 3 + self.BLOC_SIZE * 2, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)], [0, (self.platform * 4+self.BLOC_SIZE*3, self.platform*4 + self.BLOC_SIZE*3 + self.TOP_SIZE)]]]"""

        self.grid = [[(self.platform, self.platform + self.TOP_SIZE),
                        (self.platform * 2 + self.BLOC_SIZE, self.platform + self.TOP_SIZE),
                        (self.platform * 3 + self.BLOC_SIZE * 2, self.platform + self.TOP_SIZE),
                        (self.platform * 4 + self.BLOC_SIZE * 3, self.platform + self.TOP_SIZE)],

                       [(self.platform, self.platform * 2 + self.BLOC_SIZE + self.TOP_SIZE),
                        (self.platform * 2 + self.BLOC_SIZE, self.platform * 2 + self.BLOC_SIZE + self.TOP_SIZE),
                        (self.platform * 3 + self.BLOC_SIZE * 2, self.platform * 2 + self.BLOC_SIZE + self.TOP_SIZE),
                        (self.platform * 4 + self.BLOC_SIZE * 3, self.platform * 2 + self.BLOC_SIZE + self.TOP_SIZE)],

                      [(self.platform, self.platform * 3 + self.BLOC_SIZE * 2 + self.TOP_SIZE),
                       (self.platform * 2 + self.BLOC_SIZE, self.platform * 3 + self.BLOC_SIZE * 2 + self.TOP_SIZE),
                       (self.platform * 3 + self.BLOC_SIZE * 2, self.platform * 3 + self.BLOC_SIZE * 2 + self.TOP_SIZE),
                       (self.platform * 4 + self.BLOC_SIZE * 3, self.platform * 3 + self.BLOC_SIZE * 2 + self.TOP_SIZE)],

                     [(self.platform, self.platform * 4 + self.BLOC_SIZE * 3 + self.TOP_SIZE),
                      (self.platform * 2 + self.BLOC_SIZE, self.platform * 4 + self.BLOC_SIZE * 3 + self.TOP_SIZE),
                      (self.platform * 3 + self.BLOC_SIZE * 2, self.platform * 4 + self.BLOC_SIZE * 3 + self.TOP_SIZE),
                      (self.platform * 4 + self.BLOC_SIZE * 3, self.platform * 4 + self.BLOC_SIZE * 3 + self.TOP_SIZE)]]

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

    def update_grid_left_(self):
        for b in self.blocs:
            if not b.rect.x == self.platform:
                b.rect.x -= 4


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

    def update_grid_down(self):
        for i in range(len(self.grid)):
            for n in range(len(self.grid)):
                b = 0
                if not n == 3:
                    for i in range(2):
                        if self.grid[n+b+1][i][0] == 0 and self.grid[n+b][i][0] != 0:
                            self.grid[n+b+1][i][0] = self.grid[n+b][i][0]
                            self.grid[n+b][i][0] = 0
                            b += 1
                        if n+b+1 < len(self.grid):
                            if self.grid[n+b+1][i][0] == self.grid[n+b][i][0]:
                                self.grid[n+b+1][i][0] = self.grid[n+b][i][0]*2
                                self.grid[n+b][i][0] = 0
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
        self.update_blocs_coos()
        self.screen.fill(self.background_color)
        self.screen.blit(self.background, (0, 200))
        # self.update_block_grid()
        # print(len(self.blocs))
        for bloc in self.blocs:
            pygame.draw.rect(self.screen, self.set_color(bloc.value),
                             (bloc.rect.x, bloc.rect.y, bloc.rect.width, bloc.rect.height))
            self.screen.blit(self.font_bloc.render(str(bloc.value), True, (0, 0, 0)),
                             self.set_font_position(bloc.rect.x, bloc.rect.y, bloc.value, self.font_bloc))
            bloc.blocs = self.blocs.copy()
            bloc.blocs.remove(self)
            bloc.rect_coo = (bloc.rect.x, bloc.rect.y)
            if self.direction == 'left':
                if not bloc.moved:
                    bloc.left()
            elif self.direction == 'right':
                if not bloc.moved:
                    bloc.right()
            elif self.direction == 'down':
                if not bloc.moved:
                    bloc.down()
            elif self.direction == 'up':
                if not bloc.moved:
                    bloc.up()


    def update_blocs_coos(self):
        self.blocs_coos = []
        for b in self.blocs:
            for row in self.grid:
                if b.rect_coo in row and not b.rect_coo in self.blocs_coos:
                    self.blocs_coos.append(b.rect_coo)
    def checkcollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

