import pygame as pg
import random

class Brick(pg.sprite.Sprite):
    """ Brick class

    The Brick class creates a brick that is damageable
    The ball will bounce off of it and cause damage
    """
    def __init__(self, width, height, xOffset, yOffset):
        """ Constructor for the Bumper class

        Creates a new Bumper which is descendent from pygame.sprite
        
        Arguments
        width: bumper width in pixels
        height: bumper height in pixels
        xOffset: bumper offset in the X axis in pixels
        yOffset: bumper offset in the Y axis in pixels
        """

        # initialize superclass
        super().__init__()

        # define image and set life and fill color randomly
        self.image = pg.Surface( (width - 4, height - 4) )
        r = random.randint
        self._life = r(1, 25)
        self.image.fill(Brick.getColor(self._life))

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset + 2
        self.rect.y  = yOffset + 2

        #load sound effects
        self.brickHit = pg.mixer.Sound('./sfx/425725__moogy73__click04.wav')
        self.brickDestroyed = pg.mixer.Sound('./sfx/pop.mp3')    

    def damage(self):
        """ Causes damage to the brick 
        
        The assignment specified 1 damage per hit but that seemed
        a little overkill so it is set to 5. Set the damage to
        whatever you prefer
        """
        #self.life = self.life - 1
        self._life = self._life - 5

        # if not destroyed, play standard hit sound
        if self._life > 0:
           self.brickHit.play()
           
    def update(self):
        """ Sprite update method
        
        Updates the brick internal values in preparation for rerendering
        """
        super().update(self) 

        # if the brick is dead, destory it
        if self._life <= 0:
            self.brickDestroyed.play()
            self.kill()

        # reset the color according to its current life
        self.image.fill(Brick.getColor(self._life))

    @staticmethod
    def getColor(index):
        """Static Color Decoder 
        
        Color decoder for determining brick color according to life value

        Arguments
        index: the current life value (between 1 and 25)
        """
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
        # return the color at the specified index
        # if it doesnt exist return black (0, 0, 0)
        return colors.get(index, (0, 0, 0))
