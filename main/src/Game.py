import pygame, sys
from interfaces.InterfaceManagers import InterfaceManager
from pygame.locals import *

pygame.init()

def drawScreen(SCREEN, interfaceManager):
    interfaceManager.drawInterfaces()
    pygame.display.flip()

def gameLoop():
    running = True
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    interfaceManager = InterfaceManager(SCREEN)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawScreen(SCREEN, interfaceManager)
        CLOCK.tick(FPS)