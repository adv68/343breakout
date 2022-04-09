import pygame as pg

class Bumper(pg.sprite.Sprite):
    """ Bumper class

    The Bumper class creates a brick that is not damageable
    The ball will bounce off of it, but it will not break
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

        # define image of bumper
        self.image = pg.Surface( (width - 4, height - 4) )
        self.image.fill((0, 0, 0))

        # offset rectangle in the game board
        self.rect = self.image.get_rect()
        self.rect.x = xOffset + 2
        self.rect.y  = yOffset + 2
           
    def update(self):
        """Sprite update method"""
        # call superclass update
        super().update(self) 
