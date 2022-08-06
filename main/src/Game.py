import pygame, sys
from pygame.locals import *
pygame.init()

def drawScreen(SCREEN):
    pygame.draw.rect(SCREEN, (100,100,100,100), (255,0,0))

def gameLoop():
    running = True
    WIDTH = 800
    HEIGHT = 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawScreen(SCREEN)