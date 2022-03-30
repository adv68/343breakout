import pygame as pg

from components.brick import Brick;

class Ball(pg.sprite.Sprite):
    def __init__(self):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (10, 10) )
        self.image.fill( (0, 0, 0) )
        
        # center ball in the game board
        self.rect = self.image.get_rect()
        self.rect.x = 395
        self.rect.y  = 300

        #set velocity to 3
        self.velocity = [3,-3]

        #collision logic, ball can see bricks and paddle initialized
        self.bricks = None
        self.paddle = None

    #setBricks tells the ball what bricks are out there
    def setBricks(self, bricks):
        self.bricks = bricks

    #same as above but for paddle
    def setPaddle(self, paddle):
        self.paddle = paddle

    def update(self):
        #update the balls velocity according to initializer
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #if the ball goes past the paddle, end the game
        #perhaps we should change to just updating the overlay
        if self.rect.y > 600:
            pg.quit()
            exit()
            
        #if ball touches top of screen, negate y velocity
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]

        #if ball touches left or right side of screen, negate x velocity
        #790 for boundary is used because the ball is 10 pixels wide
        if (self.rect.x <0 or self.rect.x >790):
            self.velocity[0] = -self.velocity[0]

        #more collision logic for changing ball direction
        collisions = pg.sprite.spritecollide(self, Ball.bricks, False)
        if collisions:
            for brick in collisions:
                if type(brick) is Brick:
                    brick.damage()

            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = -self.velocity[1]

        collisions2 = pg.sprite.spritecollide(self, Ball.paddle, False)
        if collisions2:
            #should reverse direction on paddle
            #self.velocity[0] = -self.velocity[0]
            self.velocity[1] = -self.velocity[1]
            
