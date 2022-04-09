import pygame as pg

from components.brick import Brick;
from random import randint;

class Ball(pg.sprite.Sprite):
    """ Ball class

    The Ball class creates a ball for the game
    The ball manages all of the game interactions including
    damage to bricks and calculating new position

    In order for the game to work properly, before using a Ball,
    a static Bricks spritegroup needs to be set and a static 
    Paddle singlespritegroup needs to be set
    """
    def __init__(self, size, stats):
        """ Constructor for the Ball class
        
        Creates a new Ball which is descendant from pygame.sprite

        Arguments
        size: the height and width in pixels of the ball
        stats: a components.Stats object that is a container for current stats
        """
        # initialize superclass
        super().__init__()

        #intialize stats
        self._stats = stats

        # define the image
        self._size = size
        self.image = pg.Surface( (size, size) )
        self.image.fill( (0, 0, 0) )
        
        # define the ball position in a random spot in the center
        self.rect = self.image.get_rect()
        self.rect.x = randint(200, 600)
        self.rect.y  = 500

        # define paddle offset variables so that the paddle reflection
        # map can vary
        self._paddleOffset = 0
        self._paddleOffsetDir = True

        #set initial velocity to 45deg left or 45deg right randomly
        dir = randint(0, 1)
        if dir == 0:
            self._velocity = [3, -3]
        else:
            self._velocity = [-3, -3]

        #load sound effects
        self.paddleOrWallHit = pg.mixer.Sound('./sfx/505613__bjoerissen__d85-conga-low-soft-bounce-1.wav')

    def getPosition(self):
        """ Get the ball position

        The ball position returned is the center of the ball, not the rectangle coordinate
        """
        return (self.rect.x + (self._size / 2), self.rect.y + (self._size / 2))

    def setBrickCollisionNewVelocity(self, brick):
        """ Calculate the ball velocity
        
        Pass in a brick that the ball collided with and passed on
        relative positions, recalulate and set the ball velocity
        """
        # get the current position and calculate the position relative to the brick sides
        # so we can see which side it collided with
        position = self.getPosition()
        topInside = position[1] - brick.rect.top
        rightInside = brick.rect.right - position[0]
        bottomInside = brick.rect.bottom - position[1]
        leftInside = position[0] - brick.rect.left
        
        # store the rel positions in a list and sort it so see which one is the collision
        ballRelPos = [topInside, rightInside, bottomInside, leftInside]
        ballRelPos.sort()

        # check to see which side made the collision and adjust velocity accordingly
        if topInside == ballRelPos[0]:
            self._velocity[1] = -self._velocity[1]
        if rightInside == ballRelPos[0]:
            self._velocity[0] = -self._velocity[0]
        if bottomInside == ballRelPos[0]:
            self._velocity[1] = -self._velocity[1]
        if leftInside == ballRelPos[0]:
            self._velocity[0] = -self._velocity[0]

    def update(self):
        """ Sprite update method
        
        Updates the ball position and velocity according to its
        various interactions with bricks, walls, and the paddle
        """

        #update the balls position according to its velocity
        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]

        #if the ball goes past the paddle, remove a life and destroy the ball
        if self.rect.y > 600:
            if self._stats.getLives() > 0:
                self.kill()
                self._stats.decrementLives()
                return
            
        #if ball touches top of screen, set y velocity positive
        if self.rect.y <= 0:
            self._velocity[1] = -self._velocity[1]
            self.paddleOrWallHit.play()

        #if ball touches left side of screen, set x velocity positive
        if self.rect.x <= 0:
            self._velocity[0] = - self._velocity[0]
            self.paddleOrWallHit.play()

        #if ball touches right side of screen, set x velocity negative
        #790 for boundary is used because the ball is 10 pixels wide
        if self.rect.x >= 790:
            self._velocity[0] = -self._velocity[0]
            self.paddleOrWallHit.play()

        #find which bricks collided
        collisions = pg.sprite.spritecollide(self, Ball.bricks, False)
        if collisions:
            for brick in collisions:
                # if the brick is a Brick (as opposed to bumper)
                if type(brick) is Brick:
                    brick.damage()
                    self._stats.appendScore(10)

                # calculate the new ball velocity
                self.setBrickCollisionNewVelocity(brick)

        #find if the paddle collided
        collisions2 = pg.sprite.spritecollide(self, Ball.paddle, False)
        if collisions2:
            # recalculate paddle offset direction
            if self._paddleOffset < -8:
                self._paddleOffsetDir = True
            elif self._paddleOffset > 8:
                self._paddleOffsetDir = False

            # calculate paddle offset
            if self._paddleOffsetDir:
                self._paddleOffset = self._paddleOffset + 1
            else:
                self._paddleOffset = self._paddleOffset - 1

            #passed on paddle position, set new velocity
            ballCenter = self.rect.x + 5
            reflectPoint = ballCenter - collisions2[0].getPosition()
            if reflectPoint < -36 + self._paddleOffset:
                self._velocity[0] = -3
                self._velocity[1] = -3
            elif reflectPoint < -6 + self._paddleOffset:
                self._velocity[0] = -1
                self._velocity[1] = -4
            elif reflectPoint < 6 + self._paddleOffset:
                self._velocity[0] = 0
                self._velocity[1] = -4
            elif reflectPoint < 36 + self._paddleOffset:
                self._velocity[0] = 1
                self._velocity[1] = -4
            else:
                self._velocity[0] = 3
                self._velocity[1] = -3

            # play sound sfx for paddle hit
            self.paddleOrWallHit.play()
        