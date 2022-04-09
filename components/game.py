import pygame as pg

from components.brick import Brick

class Game:
    def __init__(self, width, height):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode ( (width, height) )
        self.clock = pg.time.Clock()

        self.damagableBricks = pg.sprite.Group()
        
        self.bricks = pg.sprite.Group()
        self.paddle = pg.sprite.GroupSingle()
        self.ball = pg.sprite.GroupSingle()
        self.overlay = pg.sprite.GroupSingle()
        pg.mixer.music.set_volume(.3)
        pg.mixer.music.load('./sfx/happy-14585.mp3')
        pg.mixer.music.play(-1)
        
    def run(self):  
        while True:
            events = pg.event.get()
            for event in events:
                    if event.type == pg.QUIT:
                        return
            #Take events

            #Update updateable objects
            self.bricks.update()
            self.paddle.update()
            self.ball.update()

            #check if any bricks still exist
            #if not self.bricks:
            if not self.damagableBricks:
                return

            #Redraw
            self.screen.fill( (255, 255, 255) )
            self.bricks.draw(self.screen)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.overlay.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)

    def addBrick(self, brick):
        self.bricks.add(brick)
        if type(brick) is Brick:
            self.damagableBricks.add(brick)

    def setPaddle(self, paddle):
        self.paddle.add(paddle)

    def setBall(self, ball):
        self.ball.add(ball)

    def setOverlay(self, overlay):
        self.overlay.add(overlay)

    #getter for bricks for the ball to use
    def getBricks(self):
        return self.bricks

    #same as above but for paddle
    def getPaddle(self):
        return self.paddle

    def stop(self):
        self.screen.fill((0, 0, 0))
        font = pg.font.Font(pg.font.get_default_font(), 48)
        levelTxt = font.render("Level 2", True, pg.Color(255, 255, 255))
        self.screen.blit(levelTxt, ((self.width - levelTxt.get_width()) / 2, (self.height - levelTxt.get_height()) / 2))
        pg.display.flip()

    # release pygame resources
    def dispose(self):
        pg.quit()
