import pygame
from game import Game

pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((800, 1000))
game = Game(screen)

running = True
while running:
    # update game
    game.update()

    # screen actualize
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            game.mouse_down = False
        elif event.type == pygame.MOUSEMOTION:
            if game.mouse_down:
                for b in game.blocs:
                    if b.rect.collidepoint(event.pos):
                        b.rect.center = event.pos

pygame.quit()
