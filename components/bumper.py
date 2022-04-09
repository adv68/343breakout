import pygame as pg
import random

class Bumper(pg.sprite.Sprite):
    def __init__(self, width, height, xOffset, yOffset):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (width - 4, height - 4) )
        self.image.fill((0, 0, 0))

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset + 2
        self.rect.y  = yOffset + 2

        #load sound effects
        self.bumperHit = pg.mixer.Sound('./sfx/425725__moogy73__click04.wav')
           
    def update(self):
        super().update(self) 

