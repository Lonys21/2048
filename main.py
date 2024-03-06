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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.update_grid_left()
            elif event.key == pygame.K_RIGHT:
                game.update_grid_right()

pygame.quit()
