import pygame as pg

from components.brick import Brick;
from random import randint;

class Ball(pg.sprite.Sprite):
    def __init__(self, size, stats):
        # initialize superclass
        super().__init__()

        #intialize stats
        self.stats = stats

        self.size = size
        self.image = pg.Surface( (size, size) )
        self.image.fill( (0, 0, 0) )
        
        # center ball in the game board
        self.rect = self.image.get_rect()
        self.rect.x = randint(200, 600)
        self.rect.y  = 500

        self._paddleOffset = 0
        self._paddleOffsetDir = True

        #set velocity to 3
        dir = randint(0, 1)
        if dir == 0:
            self.velocity = [3, -3]
        else:
            self.velocity = [-3, -3]

        #load sound effects
        self.paddleOrWallHit = pg.mixer.Sound('./sfx/505613__bjoerissen__d85-conga-low-soft-bounce-1.wav')

    def getPosition(self):
        return (self.rect.x + (self.size / 2), self.rect.y + (self.size / 2))

    def setBrickCollisionNewVelocity(self, brick):
        position = self.getPosition()
        topInside = position[1] - brick.rect.top
        rightInside = brick.rect.right - position[0]
        bottomInside = brick.rect.bottom - position[1]
        leftInside = position[0] - brick.rect.left
        ballRelPos = [topInside, rightInside, bottomInside, leftInside]
        ballRelPos.sort()
        if topInside == ballRelPos[0]:
            self.velocity[1] = -self.velocity[1]
        if rightInside == ballRelPos[0]:
            self.velocity[0] = -self.velocity[0]
        if bottomInside == ballRelPos[0]:
            self.velocity[1] = -self.velocity[1]
        if leftInside == ballRelPos[0]:
            self.velocity[0] = -self.velocity[0]

    def update(self):
        #update the balls velocity according to initializer
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #if the ball goes past the paddle, end the game
        #perhaps we should change to just updating the overlay
        if self.rect.y > 600:
            if self.stats.getLives() > 0:
                self.kill()
                self.stats.decrementLives()
                return

            if self.stats.getLives() <= 0:
                pg.quit()
                exit()
            
        #if ball touches top of screen, set y velocity positive
        #sometimes the ball glitches past, so negation can loop it in the wall
        #manually setting the velocity is safer
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]
            self.paddleOrWallHit.play()

        #if ball touches left side of screen, set x velocity positive
        if self.rect.x <= 0:
            self.velocity[0] = - self.velocity[0]
            self.paddleOrWallHit.play()

        #if ball touches right side of screen, set x velocity negative
        #790 for boundary is used because the ball is 10 pixels wide
        if self.rect.x >= 790:
            #self.velocity[0] = -3
            self.velocity[0] = -self.velocity[0]
            self.paddleOrWallHit.play()

        #more collision logic for changing ball direction
        collisions = pg.sprite.spritecollide(self, Ball.bricks, False)
        if collisions:
            for brick in collisions:
                if type(brick) is Brick:
                    brick.damage()
                    self.setBrickCollisionNewVelocity(brick)
                    #increase score by 10
                    self.stats.appendScore(10)
                else:
                    self.setBrickCollisionNewVelocity(brick)

        collisions2 = pg.sprite.spritecollide(self, Ball.paddle, False)
        if collisions2:
            # recalculate paddle offset
            if self._paddleOffset < -8:
                self._paddleOffsetDir = True
            elif self._paddleOffset > 8:
                self._paddleOffsetDir = False

            if self._paddleOffsetDir:
                self._paddleOffset = self._paddleOffset + 1
            else:
                self._paddleOffset = self._paddleOffset - 1

            #should reverse direction on paddle
            ballCenter = self.rect.x + 5
            reflectPoint = ballCenter - collisions2[0].getPosition()
            if reflectPoint < -36 + self._paddleOffset:
                self.velocity[0] = -3
                self.velocity[1] = -3
            elif reflectPoint < -6 + self._paddleOffset:
                self.velocity[0] = -1
                self.velocity[1] = -4
            elif reflectPoint < 6 + self._paddleOffset:
                self.velocity[0] = 0
                self.velocity[1] = -4
            elif reflectPoint < 36 + self._paddleOffset:
                self.velocity[0] = 1
                self.velocity[1] = -4
            else:
                self.velocity[0] = 3
                self.velocity[1] = -3
            self.paddleOrWallHit.play()
            
