import pygame as pg

class Game:
    def __init__(self, width, height):
        pg.init()
        self.__running = False
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode ( (width, height) )
        self.clock = pg.time.Clock()
        self.bricks = pg.sprite.Group()
        self.paddle = pg.sprite.GroupSingle()
        
    def run(self):
        while self.__running:
            events = pg.event.get()
            for event in events:
                    if event.type == pg.QUIT:
                        self.__running = False
                        pg.quit()
                        exit()
            #Take events
			
            #Update updateable objects
            self.bricks.update()
            self.paddle.update()
            #Redraw
            self.screen.fill( (255, 255, 255) )
            self.bricks.draw(self.screen)
            self.paddle.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)

    def setRunning(self, running):
        self.__running = running

    def addBrick(self, brick):
        self.bricks.add(brick)

    def setPaddle(self, paddle):
        self.paddle.add(paddle)