import pygame

class Bloc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, value, id):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/Player.png')
        self.image = pygame.transform.scale(self.image, (self.game.BLOC_SIZE, self.game.BLOC_SIZE))
        self.rect = pygame.rect.Rect(x, y, self.game.BLOC_SIZE, self.game.BLOC_SIZE)
        self.rect_coo = (self.rect.x, self.rect.y)
        self.blocs = pygame.sprite.Group()
        self.value = value
        self.moved = True
        self.fusion_possible = False
        self.fusionned = False
        self.velocity = 4
        self.id = id

    def left(self):
        if not self.rect.x == self.game.platform:
            if not (self.rect.x - self.game.BLOC_SIZE - self.game.platform, self.rect.y) in self.game.blocs_coos and not self.fusion_possible:
                self.rect.x -= self.velocity
            else:
                for b in self.game.blocs:
                    if self.rect.x - self.game.BLOC_SIZE - self.game.platform == b.rect.x and self.rect.y == b.rect.y:
                        if b.value == self.value and b.id != self.id and not b.fusionned:
                            self.fusion_possible = True
                            self.fusion_bloc = b
            if self.fusion_possible:
                if self.rect.x <= self.fusion_bloc.rect.centerx:
                    self.fusion_bloc.fusionned = True
                    self.fusion_bloc.value = self.value * 2
                    self.game.blocs.remove(self)
                else:
                    self.rect.x -= self.velocity
        else:
            self.moved = True

    def right(self):
        if not self.rect.x == self.game.platform*4 + self.game.BLOC_SIZE*3:
            if not (self.rect.x + self.game.BLOC_SIZE + self.game.platform, self.rect.y) in self.game.blocs_coos and not self.fusion_possible:
                self.rect.x += self.velocity
            else:
                for b in self.game.blocs:
                    if self.rect.x + self.game.BLOC_SIZE + self.game.platform == b.rect.x and self.rect.y == b.rect.y:
                        if b.value == self.value and b.id != self.id and not b.fusionned:
                            self.fusion_possible = True
                            self.fusion_bloc = b
            if self.fusion_possible:
                if self.rect.x + self.rect.width >= self.fusion_bloc.rect.centerx:
                    self.fusion_bloc.fusionned = True
                    self.fusion_bloc.value = self.value * 2
                    self.game.blocs.remove(self)
                else:
                    self.rect.x += self.velocity
        else:
            self.moved = True



    def close_case(self):
        close_x = 10000
        for line in self.game.grid:
            for case in line:
                if case[0] - self.rect.x < close_x and case[0] - self.rect.x > 0:
                    close_x = case[0] - self.rect.x
                    close_case = case
            return close_case
