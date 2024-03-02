import pygame

class Bloc(pygame.sprite.Sprite):
    def __init__(self, game, x, y, value):
        self.game = game
        self.rect = pygame.rect.Rect(x, y, self.game.BLOC_SIZE, self.game.BLOC_SIZE)
        self.value = value