import pygame as pg
import random

class Brick(pg.sprite.Sprite):
    def __init__(self, xOffset, yOffset):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (100, 50) )
        r = random.randint
        self.image.fill( (r(0,254), r(0,254), r(0,254)) )

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset
        self.rect.y  = yOffset