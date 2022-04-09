import pygame as pg
import random

class Brick(pg.sprite.Sprite):
    def __init__(self, width, height, xOffset, yOffset):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (width - 6, height - 6) )
        r = random.randint
        self.life = r(1, 25)
        self.image.fill(Brick.getColor(self.life))

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset + 3
        self.rect.y  = yOffset + 3

        #load sound effects
        self.brickHit = pg.mixer.Sound('./sfx/425725__moogy73__click04.wav')
        self.brickDestroyed = pg.mixer.Sound('./sfx/pop.mp3')    

    def damage(self):
        #self.life = self.life - 1
        self.life = self.life - 5
        if self.life > 0:
           self.brickHit.play()
           
    def update(self):
        super().update(self) 

        if self.life <= 0:
            self.brickDestroyed.play()
            self.kill()

        self.image.fill(Brick.getColor(self.life))

    @staticmethod
    def getColor(index):
        colors = {
            25: (126, 56, 96),
            24: (194, 38, 165),
            23: (169, 34, 210),
            22: (77, 32, 155),
            21: (53, 24, 181),
            20: (57, 39, 220),
            19: (53, 103, 240),
            18: (25, 148, 214),
            17: (28, 198, 241),
            16: (19, 219, 172),
            15: (30, 234, 142),
            14: (17, 231, 106),
            13: (20, 218, 46),
            12: (93, 248, 10),
            11: (162, 235, 17),
            10: (208, 243, 9),
            9:  (240, 236, 12),
            8:  (237, 221, 0),
            7:  (238, 192, 11),
            6:  (233, 148, 10),
            5:  (241, 141, 11),
            4:  (235, 125, 14),
            3:  (224, 89, 17),
            2:  (237, 53, 11),
            1:  (240, 10, 10)
        }
        return colors.get(index, (0, 0, 0))

