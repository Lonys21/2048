import pygame

class Bloc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, value, id):
        super().__init__()
        self.game = game
        """self.image = pygame.image.load('assets/Player.png')
        self.image = pygame.transform.scale(self.image, (self.game.BLOC_SIZE, self.game.BLOC_SIZE))"""
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
                        if b.id != self.id:
                            if b.value == self.value and not b.fusionned:
                                self.fusion_possible = True
                                self.fusion_bloc = b
                            else:
                                self.moved = True
                if self.fusion_possible and not self.fusion_bloc.fusionned and not self.fusionned:
                    if self.rect.x <= self.fusion_bloc.rect.centerx and self.fusion_bloc in self.game.blocs:
                        self.fusion_bloc.fusionned = True
                        self.fusion_bloc.value = self.value * 2
                        self.fusion_bloc.moved = True
                        self.game.blocs.remove(self)
                    else:
                        self.rect.x -= self.velocity
        else:
            self.moved = True

    def right(self):
        if not self.rect.x == self.game.platform*4 + self.game.BLOC_SIZE*3: # Not the rightest block
            if not (self.rect.x + self.game.BLOC_SIZE + self.game.platform, self.rect.y) in self.game.blocs_coos and not self.fusion_possible: # not block to the right
                self.rect.x += self.velocity # go to the right
            else:
                for b in self.game.blocs:
                    if self.rect.x + self.game.BLOC_SIZE + self.game.platform == b.rect.x and self.rect.y == b.rect.y: #  find the block to the right
                        if b.id != self.id:
                            if b.value == self.value:
                                if not b.fusionned and not b.fusion_possible: # if same number, and not the right block already fusionned and not the right block fusionning
                                    self.fusion_possible = True
                                    self.fusion_bloc = b
                                else:
                                    self.fusion_possible = False
                            elif b.moved:
                                self.moved = True
            if self.fusion_possible and not self.fusion_bloc.fusion_possible and not self.fusionned: # fusion possible and not the right block already fussionning and not myself already fussionned
                if self.rect.x + self.rect.width >= self.fusion_bloc.rect.centerx and self.fusion_bloc in self.game.blocs: # If I'm beyond his center and the block exist
                    self.fusion_bloc.fusionned = True
                    self.fusion_bloc.value = self.value * 2 # fusionner value Double
                    self.fusion_bloc.moved = True
                    self.game.blocs.remove(self) # delete myself
                else:
                    self.rect.x += self.velocity # go to the right
            else:
                self.fusion_possible = False

        else:
            self.moved = True

    def down(self):
        if not self.rect.y == self.game.TOP_SIZE + self.game.platform*4 + self.game.BLOC_SIZE*3:
            if not (self.rect.x, self.rect.y + self.game.BLOC_SIZE + self.game.platform) in self.game.blocs_coos and not self.fusion_possible:
                self.rect.y += self.velocity
            else:
                for b in self.game.blocs:
                    if self.rect.y + self.game.BLOC_SIZE + self.game.platform == b.rect.y and self.rect.x == b.rect.x:
                        if b.id != self.id:
                            if b.value == self.value and not b.fusionned:
                                self.fusion_possible = True
                                self.fusion_bloc = b
                            else:
                                self.moved = True
            if self.fusion_possible and not self.fusion_bloc.fusion_possible and not self.fusionned:
                if self.rect.y + self.rect.width >= self.fusion_bloc.rect.centery:
                    self.fusion_bloc.fusionned = True
                    self.fusion_bloc.value = self.value * 2
                    self.fusion_bloc.moved = True
                    self.game.blocs.remove(self)
                else:
                    self.rect.y += self.velocity
            else:
                self.fusion_possible = False
        else:
            self.moved = True

    def up(self):
        if not self.rect.y == self.game.TOP_SIZE + self.game.platform:
            if not (self.rect.x, self.rect.y - self.game.BLOC_SIZE - self.game.platform) in self.game.blocs_coos and not self.fusion_possible:
                self.rect.y -= self.velocity
            else:
                for b in self.game.blocs:
                    if self.rect.y - self.game.BLOC_SIZE - self.game.platform == b.rect.y and self.rect.x == b.rect.x:
                        if b.id != self.id:
                            if b.value == self.value and not b.fusionned:
                                b.fusionned = True
                                self.fusion_possible = True
                                self.fusion_bloc = b
                            else:
                                self.moved = True
            if self.fusion_possible and not self.fusion_bloc.fusion_possible and not self.fusionned:
                if self.rect.y <= self.fusion_bloc.rect.centery:
                    self.fusion_bloc.fusionned = True
                    self.fusion_bloc.value = self.value * 2
                    self.fusion_bloc.moved = True
                    self.game.blocs.remove(self)
                else:
                    self.rect.y -= self.velocity
            else:
                self.fusion_possible = False
        else:
            self.moved = True


