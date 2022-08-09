from dataclasses import dataclass
import pygame
from interfaces.Interfaces import Interface

class InterfaceManager():
    def __init__(self, dest) -> None:
        self.SCREEN = dest
        self.interfaces = [Interface(200, 300)]
        
    def drawInterfaces(self):
        for interface in self.interfaces:
            self.SCREEN.blit(interface.image, interface.image.get_rect())