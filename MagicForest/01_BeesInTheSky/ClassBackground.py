import pygame
from Config import *


class Background():

    def __init__(self):
        # Create the sky image
        self.skyImage = pygame.image.load(SPRITESHEET_PATH + "Background/Background.png").convert()
        self.skyImage = pygame.transform.scale(self.skyImage, (WINDOW_WIDTH, WINDOW_HEIGHT))


    def draw(self, displaySurface):
        # Draw sky image
        displaySurface.blit(self.skyImage, (0, 0))
