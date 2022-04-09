import pygame as pg

from components.brick import Brick
from components.stats import Stats
from components.ball import Ball
from components.paddle import Paddle
from components.overlay import Overlay
from time import time

class Game:
    """ Game class

    The game class creates a new pygame instance

    The game class can be reused for levels and other things:

    gameMessage displays a full screen message
    run runs the game until all the game bricks are destroyed
    showHelp displays the help screen
    """
    def __init__(self, width, height):
        """ Constructor for Game class

        Creates a new Game instance

        Arguments
        width: width of the game window in pixels
        height: height of game window in pixels
        """
        # initialize pygame and create new window and clock
        pg.init()
        self._width = width
        self._height = height
        self.screen = pg.display.set_mode ( (width, height) )
        self.clock = pg.time.Clock()
        
        # define containers for the game components
        self._bricks = pg.sprite.Group()
        self._damageableBricks = pg.sprite.Group()
        self._balls = pg.sprite.Group()
        self._paddle = pg.sprite.GroupSingle()
        self._overlay = pg.sprite.GroupSingle()

        # create a new stats object
        self.stats = Stats(5, 0)   
        self.bonusBalls = 0

        # add a new paddle and overlay to their containers
        self._paddle.add(Paddle(width / 5, 8))  
        self._overlay.add(Overlay(self.stats))

        # define the Ball statics
        # bricks and paddle so the ball can do its collision logic
        Ball.bricks = self._bricks
        Ball.paddle = self._paddle

    def run(self, level):  
        """ Run game loop

        The run loop runs the game until all the bricks are destroyed
        For five seconds, the screen shows whatever is in level

        Arguments
        level: the level text to display

        Returns false if the game is over or killed, true if we can proceed on
        """
        # if there are any remaining balls from the previous level, get rid of them
        self._balls.empty()

        # set game start time to 5 seconds from now
        startTime = time() + 5

        # start sfx
        pg.mixer.music.set_volume(.3)
        pg.mixer.music.load('./sfx/happy-14585.mp3')
        pg.mixer.music.play(-1)

        # define paused as false
        paused = False

        # forever unless we return
        while True:
            # loop through events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return False
                elif event.type == pg.KEYDOWN:
                    # 'b' creates new balls
                    if event.key == pg.K_b:
                        self._balls.add(Ball(9, self.getStats()))
                    # spacebar does pause/unpause
                    elif event.key == pg.K_SPACE:
                        paused = not paused

            # If the level start delay hasn't passed
            if time() < startTime:
                self.screen.fill((0, 0, 0))
                font = pg.font.Font(pg.font.get_default_font(), 48)
                levelTxt = font.render(level, True, pg.Color(255, 255, 255))
                self.screen.blit(levelTxt, ((self._width - levelTxt.get_width()) / 2, (self._height - levelTxt.get_height()) / 2))
            # If paused, then freeze the screen
            elif paused:
                font = pg.font.Font(pg.font.get_default_font(), 72)
                pausedTxt = font.render('Paused', True, pg.Color(0, 0, 0))
                self.screen.blit(pausedTxt, ((self._width - pausedTxt.get_width()) / 2, (self._height - pausedTxt.get_height()) / 2))
            # If playing and not paused
            else:
                # Update updateable objects
                self._bricks.update()
                self._paddle.update()
                self._balls.update()
                self._overlay.update()

                # Check score to see if eligable for a bonus life
                if self.stats.getScore() // 1000 > self.bonusBalls:
                    self.bonusBalls = self.bonusBalls + 1
                    self.stats.incrementLives()

                # Check if we are out of lives
                # If we are exit and return false
                if self.stats.getLives() <= 0:
                    return False

                # If no balls exist, spawn another one
                if not self._balls:
                    self._balls.add(Ball(9, self.getStats()))

                #check if any bricks still exist
                if not self._damageableBricks:
                    # clear out any non-damageable bricks
                    self._bricks.empty()
                    return True

                #Redraw
                self.screen.fill((255, 255, 255))
                self._bricks.draw(self.screen)
                self._paddle.draw(self.screen)
                self._balls.draw(self.screen)
                self._overlay.draw(self.screen)

            # flip display and wait for clock
            pg.display.flip()
            self.clock.tick(60)

    def gameMessage(self, message, duration):
        """ Display a game message

        Displays a full screen message for x seconds

        Arguments
        message: the game message to display
        duration: the amount of time in seconds for the message to show

        Returns false if exited, true if expired on timeout
        """

        # set message end time to specified seconds from now
        startTime = time() + duration

        # draw message
        self.screen.fill((0, 0, 0))
        font = pg.font.Font(pg.font.get_default_font(), 48)
        levelTxt = font.render(message, True, pg.Color(255, 255, 255))
        self.screen.blit(levelTxt, ((self._width - levelTxt.get_width()) / 2, (self._height - levelTxt.get_height()) / 2))

        # loop until timeout
        while True:
            # loop through events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return False

            # If the end time has passed then exit
            if time() > startTime:
                return True

            # flip display and tick clock
            pg.display.flip()
            self.clock.tick(60)

    def showHelp(self):
        """ Show help screen

        Display the help screen
        Whatever is defined in the directions dictionary will
        b displayed

        Returns false if cancelled, true if proceed
        """
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

        # draw the Directions title
        self.screen.fill((0, 0, 0))
        font = pg.font.Font(pg.font.get_default_font(), 48)
        titleTxt = font.render('Directions', True, pg.Color(255, 255, 255))
        self.screen.blit(titleTxt, (30, 30))

        # loop through the direction lines and draw them
        lineOffset = 100
        font = pg.font.Font(pg.font.get_default_font(), 24)
        for line in directions:
            lineTxt = font.render(line, True, pg.Color(255, 255, 255))
            self.screen.blit(lineTxt, (30, lineOffset))
            lineOffset = lineOffset + 40

        # run event loop until quit or proceed key
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

    def dispose(self):
        """Dispose pygame resources"""
        pg.quit()

    def getStats(self):
        """Get stats object"""
        return self.stats

    def getBricks(self):
        """Get bricks container"""
        return self._bricks
    
    def getPaddle(self):
        """Get paddle container"""
        return self._paddle

    def addBrick(self, brick):
        """Add a brick to the bricks container"""
        self._bricks.add(brick)
        if type(brick) is Brick:
            self._damageableBricks.add(brick)

    def setPaddle(self, paddle):
        """Set the paddle"""
        self._paddle.add(paddle)

    def addBall(self, ball):
        """Add a ball"""
        self._balls.add(ball)

    def setOverlay(self, overlay):
        """Set the overlay"""
        self._overlay.add(overlay)