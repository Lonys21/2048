import pygame

class Bloc(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.rect = pygame.rect.Rect(0, 0, 100, 100)
        self.value = 20