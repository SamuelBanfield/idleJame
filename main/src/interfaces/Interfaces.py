import pygame

class Interface():
    def __init__(self, width, height) -> None:
        self.WIDTH, self.HEIGHT = width, height
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill((0,255,0))