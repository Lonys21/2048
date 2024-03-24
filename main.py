import pygame
from game import Game

pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((800, 1000))
clock = pygame.time.Clock()
FPS = 60
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
        elif event.type == pygame.KEYDOWN and game.verify_all_moved():
            if event.key == pygame.K_LEFT:
                for b in game.blocs:
                    b.moved = False
                    b.fusion_possible = False
                    b.fusionned = False
                game.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                for b in game.blocs:
                    b.moved = False
                    b.fusion_possible = False
                    b.fusionned = False
                game.direction = 'right'
            elif event.key == pygame.K_DOWN:
                for b in game.blocs:
                    b.moved = False
                    b.fusion_possible = False
                    b.fusionned = False
                game.direction = 'down'
            elif event.key == pygame.K_UP:
                for b in game.blocs:
                    b.moved = False
                    b.fusion_possible = False
                    b.fusionned = False
                game.direction = 'up'

    clock.tick(FPS)

pygame.quit()
