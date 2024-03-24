import pygame
import random
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

        # Grid
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

        # Blocs
        self.direction = ''
        self.bloc = Bloc(self, self.platform, 216, 2, 0)
        self.bloc2 = Bloc(self, self.platform, 412, 2, 1)
        self.bloc3 = Bloc(self, self.platform, 608, 4, 2)
        self.bloc4 = Bloc(self, self.platform*2 + self.BLOC_SIZE, self.TOP_SIZE + self.platform, 2, 3)
        self.bloc5 = Bloc(self, self.platform*3 + self.BLOC_SIZE*2, self.TOP_SIZE + self.platform, 2, 4)
        self.bloc6 = Bloc(self, self.platform*4 + self.BLOC_SIZE*3, self.TOP_SIZE + self.platform, 2, 5)
        self.blocs = pygame.sprite.Group()
        i = 0
        n = 2
        for row in self.grid:
            n *= 2
            for coo in row:
                self.blocs.add(Bloc(self, coo[0], coo[1], n, i))
                i += 1
                self.font_bloc = pygame.font.SysFont("Arial", 40)
                self.blocs_coos = []



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
        for bloc in self.blocs:
            pygame.draw.rect(self.screen, self.set_color(bloc.value),
                             (bloc.rect.x, bloc.rect.y, bloc.rect.width, bloc.rect.height))
            self.screen.blit(self.font_bloc.render(str(bloc.value), True, (0, 0, 0)),
                             self.set_font_position(bloc.rect.x, bloc.rect.y, bloc.value, self.font_bloc))
            bloc.blocs = self.blocs.copy()
            bloc.blocs.remove(self)
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
            bloc.rect_coo = (bloc.rect.x, bloc.rect.y)
            self.update_blocs_coos()


    def update_blocs_coos(self):
        self.blocs_coos = []
        for b in self.blocs:
            for row in self.grid:
                if b.rect_coo in row and not b.rect_coo in self.blocs_coos:
                    self.blocs_coos.append(b.rect_coo)
    def checkcollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def verify_all_moved(self):
        a = 0
        for b in self.blocs:
            if b.moved:
                a += 1
        if a == len(self.blocs):
            return True
        return False

