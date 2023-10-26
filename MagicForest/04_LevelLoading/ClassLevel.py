import pygame
from pytmx.util_pygame import load_pygame
from Config import *
from ClassHero import Hero
from ClassBee import Bee
from ClassTile import Tile
from ClassBackground import Background


class Level():
    def __init__(self, displaySurface):
        # Load the level tmx file
        self.levelData = load_pygame(LEVELS_PATH + "Level1/level.tmx")

        # Instantiate classes
        self.background = Background()

        # Create spriteGroups
        self.hero = pygame.sprite.GroupSingle()
        self.bees = pygame.sprite.Group()
        self.platformTiles = pygame.sprite.Group()

        layer = self.levelData.get_layer_by_name('Platforms')
        for x, y, tileSurface in layer.tiles():
            tile = Tile((x * TILESIZE, y * TILESIZE), tileSurface)
            self.platformTiles.add(tile)

        self.hero.add(Hero((32, 464), faceRight = True))
        self.bees.add(Bee((200, 200), moveRight = True))
        self.bees.add(Bee((300, 380), moveRight = False))

        self.displaySurface = displaySurface


    def update(self):
        self.hero.update(self)
        self.bees.update(self)


    def draw(self):
        self.background.draw(self.displaySurface)
        self.platformTiles.draw(self.displaySurface)
        self.hero.draw(self.displaySurface)
        self.bees.draw(self.displaySurface)


    def run(self):
        self.update()
        self.draw()
