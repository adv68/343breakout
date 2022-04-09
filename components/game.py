import pygame as pg

from components.brick import Brick
from components.stats import Stats
from components.ball import Ball
from components.paddle import Paddle
from components.overlay import Overlay
from time import time

class Game:
    """
    """
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode ( (width, height) )
        self.clock = pg.time.Clock()
        
        self.bricks = pg.sprite.Group()
        self.damageableBricks = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.paddle = pg.sprite.GroupSingle()
        self.overlay = pg.sprite.GroupSingle()

        self.stats = Stats(5, 0)   
        self.bonusBalls = 0

        self.paddle.add(Paddle(width / 5, 8))  
        self.overlay.add(Overlay(self.stats))

        Ball.bricks = self.bricks
        Ball.paddle = self.paddle

    def run(self, level):  
        # if there are any remaining balls from the previous level, get rid of them
        self.balls.empty()

        # set game start time to 5 seconds from now
        startTime = time() + 5

        # start sfx
        pg.mixer.music.set_volume(.3)
        pg.mixer.music.load('./sfx/happy-14585.mp3')
        pg.mixer.music.play(-1)

        paused = False

        while True:
            # loop through events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_b:
                        self.balls.add(Ball(9, self.getStats()))
                    elif event.key == pg.K_SPACE:
                        paused = not paused

            # If the level start delay hasn't passed
            if time() < startTime:
                self.screen.fill((0, 0, 0))
                font = pg.font.Font(pg.font.get_default_font(), 48)
                levelTxt = font.render(level, True, pg.Color(255, 255, 255))
                self.screen.blit(levelTxt, ((self.width - levelTxt.get_width()) / 2, (self.height - levelTxt.get_height()) / 2))
            elif paused:
                font = pg.font.Font(pg.font.get_default_font(), 72)
                pausedTxt = font.render('Paused', True, pg.Color(0, 0, 0))
                self.screen.blit(pausedTxt, ((self.width - pausedTxt.get_width()) / 2, (self.height - pausedTxt.get_height()) / 2))
            else:
                # Update updateable objects
                self.bricks.update()
                self.paddle.update()
                self.balls.update()
                self.overlay.update()

                # Check score to see if eligable for a bonus life
                if self.stats.getScore() // 1000 > self.bonusBalls:
                    self.bonusBalls = self.bonusBalls + 1
                    self.stats.incrementLives()

                # Check if we are out of lives
                # If we are exit and return false
                if self.stats.getLives() <= 0:
                    return False

                # If no balls exist, spawn another one
                if not self.balls:
                    self.balls.add(Ball(9, self.getStats()))

                #check if any bricks still exist
                if not self.damageableBricks:
                    # clear out any non-damageable bricks
                    self.bricks.empty()
                    return True

                #Redraw
                self.screen.fill((255, 255, 255))
                self.bricks.draw(self.screen)
                self.paddle.draw(self.screen)
                self.balls.draw(self.screen)
                self.overlay.draw(self.screen)

            pg.display.flip()
            self.clock.tick(60)

    def gameMessage(self, message, duration):
        # set message end time to specified seconds from now
        startTime = time() + duration

        self.screen.fill((0, 0, 0))
        font = pg.font.Font(pg.font.get_default_font(), 48)
        levelTxt = font.render(message, True, pg.Color(255, 255, 255))
        self.screen.blit(levelTxt, ((self.width - levelTxt.get_width()) / 2, (self.height - levelTxt.get_height()) / 2))

        while True:
            # loop through events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return False

            # If the end time has passed then exit
            if time() > startTime:
                return False

            pg.display.flip()
            self.clock.tick(60)

    def showHelp(self):
        directions = [
            'Welcome to Breakout!',
            '  Break all the bricks to move on to the next level.',
            '  The paddle is controlled by your mouse.',
            '  Don\'t let the ball fall below your paddle or you will lose a life.',
            '  Extra lives are awarded for every 1000 points.',
            '  Black bricks are Bumpers - they are not damaged by hits', 
            '    and you will have to work around them.',
            '  Press \'B\' for extra balls. You are allowed as many as you like,',
            '    but be warned, each ball that you lose counts as a life!',
            '  Finally, press the spacebar to pause or unpause at any time.',
            'Best of luck - get breakin!',
            'Press ENTER to continue...'
        ]

        self.screen.fill((0, 0, 0))
        font = pg.font.Font(pg.font.get_default_font(), 48)
        titleTxt = font.render('Directions', True, pg.Color(255, 255, 255))
        self.screen.blit(titleTxt, (30, 30))

        lineOffset = 100
        font = pg.font.Font(pg.font.get_default_font(), 24)
        for line in directions:
            lineTxt = font.render(line, True, pg.Color(255, 255, 255))
            self.screen.blit(lineTxt, (30, lineOffset))
            lineOffset = lineOffset + 40

        while True:
            # loop through events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        return True

            pg.display.flip()
            self.clock.tick(60)

    # release pygame resources
    def dispose(self):
        pg.quit()

    def getStats(self):
        return self.stats

    def getBricks(self):
        return self.bricks
    
    def getPaddle(self):
        return self.paddle

    def addBrick(self, brick):
        self.bricks.add(brick)
        if type(brick) is Brick:
            self.damageableBricks.add(brick)

    def setPaddle(self, paddle):
        self.paddle.add(paddle)

    def addBall(self, ball):
        self.balls.add(ball)

    def setOverlay(self, overlay):
        self.overlay.add(overlay)