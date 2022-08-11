import pygame, sys
from interfaces.InterfaceManagers import InterfaceManager
from pygame.locals import *

from EventHandler import EventHandler
from Gamestate import GameState

pygame.init()

def drawScreen(SCREEN, interfaceManager, state):
    interfaceManager.drawInterfaces(state)
    pygame.display.flip()

def gameLoop():
    running = True
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    interfaceManager = InterfaceManager(SCREEN)
    eventHandler = EventHandler(interfaceManager)
    # My idea with this variable is it contains all of the information from the game,
    # this should make this function a bit cleaner as there won't be as many loose variables
    # hanging around, and also makes it easier to code independently as all the code for 
    # drawing the screen can be contained within the interfaces manager, so this file shouldn't
    # really need to change at all now?
    state = GameState()
    while running:
        eventHandler.handle(pygame.event.get())
        state.update()
        drawScreen(SCREEN, interfaceManager, state)
        CLOCK.tick(FPS)