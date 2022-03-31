import pygame as pg
import random

class Brick(pg.sprite.Sprite):
    def __init__(self, xOffset, yOffset):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (100, 50) )
        r = random.randint
        valueOne = r(0,254)
        valueTwo = r(0,254)
        valueThree = r(0,254)
        self.image.fill( (valueOne, valueTwo, valueThree) )
        self.hitPoints = valueOne + valueTwo + valueThree
        #we could use this code if we wanted to correlate brick color and HP
        #self.image.fill(self.hitPoints)

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset
        self.rect.y  = yOffset

        #load sound effects
        self.brickHit = pg.mixer.Sound('./sfx/425725__moogy73__click04.wav')
        self.brickDestroyed = pg.mixer.Sound('./sfx/pop.mp3')

    def damage(self):
        #self.hitPoints = self.hitPoints - 25
        self.hitPoints = self.hitPoints - 200
        if(self.hitPoints>0):
           self.brickHit.play()
           
    def update(self):
        super().update(self) 

        if self.hitPoints <= 0:
            self.brickDestroyed.play()
            self.kill()

