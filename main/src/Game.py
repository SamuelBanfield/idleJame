import pygame, sys
from pygame.locals import *
pygame.init()

def drawScreen(SCREEN):
    pygame.draw.rect(SCREEN, (255,0,0), (100,100,100,100))
    pygame.display.flip()

def gameLoop():
    running = True
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawScreen(SCREEN)
        CLOCK.tick(FPS)