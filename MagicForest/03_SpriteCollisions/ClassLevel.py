import pygame
from Config import *
from ClassHero import Hero
from ClassBee import Bee
from ClassBackground import Background


class Level():
    def __init__(self, displaySurface):

        # Instantiate classes
        self.background = Background()

        # Create spriteGroups
        self.hero = pygame.sprite.GroupSingle()
        self.bees = pygame.sprite.Group()

        self.hero.add(Hero((400,400), faceRight = True))
        self.bees.add(Bee((200, 200), moveRight = True))
        self.bees.add(Bee((300, 380), moveRight = False))

        self.displaySurface = displaySurface


    def update(self):
        self.hero.update(self)
        self.bees.update(self)


    def draw(self):
        self.background.draw(self.displaySurface)
        self.hero.draw(self.displaySurface)
        self.bees.draw(self.displaySurface)


    def run(self):
        self.update()
        self.draw()
