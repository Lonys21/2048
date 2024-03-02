import pygame

pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((1000, 1000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
