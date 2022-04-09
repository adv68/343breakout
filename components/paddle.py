import pygame as pg

class Paddle(pg.sprite.Sprite):
    """ Paddle class
    
    The Paddle class creates the user controlled paddle at the
    bottom of the screen
    """
    def __init__(self, width, speed):
        """ Constructor for the Paddle class
        
        Creates a new paddle which is descendent from pygame.sprite

        Arguments
        width: the width that the paddle should be in pixels
        speed: the max speed in pixels per frame that the paddle can travel
        """
        # initialize superclass
        super().__init__()

        # define the image of the paddle
        self.image = pg.Surface( (width, 10) )
        self.image.fill( (0, 0, 0) )
        
        # define the paddle position
        self.rect = self.image.get_rect()
        self.rect.x = 400 - (width / 2)
        self.rect.y = 550

        # copy the speed and with params
        self._speed = speed
        self._width = width

    def setPosition(self, x):
        """ Set the position of the paddle

        Coordinates are based off of the center of the paddle
        SO... if the paddle is 200px wide and the x-pos is 100, the paddle will touch the edge
        """
        self.rect.x = x - (self._width / 2)

    def getPosition(self):
        """ Get the position of the paddle
        
        The returned position is the center of the paddle
        """
        return self.rect.x + (self._width / 2)

    def update(self):
        """ Sprite update method
        
        This method updates the internal data according to the
        current game state in preparation for re-rendering
        """
        # call superclass update
        super().update(self)

        # get the mouse x position, discard y
        mouseX, _ = pg.mouse.get_pos()

        # if the paddle would be off screen, change the coordinate
        # so that it is touching the edge
        if mouseX <= self._width / 2:
            mouseX = self._width / 2
        elif mouseX >= 800 - self._width / 2:
            mouseX = 800 - self._width / 2

        # move the mouse at the defined speed toward the target position
        # since the paddle speed is restricted, the paddle will track slower
        # than the mouse if the mouse is moved too fast
        if abs(mouseX - self.getPosition()) >= self._speed:
            if mouseX < self.getPosition():
                self.setPosition(self.getPosition() - self._speed)
            elif mouseX > self.getPosition():
                self.setPosition(self.getPosition() + self._speed)
                