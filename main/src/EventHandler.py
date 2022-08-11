import pygame, sys
from interfaces.InterfaceManagers import InterfaceManager

pygame.init()

class EventHandler:
    def __init__(self, interfaceManager):
        self.interfaceManager = interfaceManager

    def handle(self, eventList):
        for event in eventList:
            self.handleEvent(event)

    def handleEvent(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
