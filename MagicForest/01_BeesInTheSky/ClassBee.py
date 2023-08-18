import pygame
from Config import *


class Bee():

    def __init__(self, position):

        beesImage = pygame.image.load(SPRITESHEET_PATH + "/Mob/Small bee/Fly/Fly-Sheet.png").convert_alpha()
        self.image =beesImage.subsurface(pygame.Rect(16, 0, 48, 48))
        self.rect = self.image.get_rect(bottomleft = position)


    def update(self, level):
        pass


    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)
        