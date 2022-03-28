# Main file to run the breakout game
# TODO Add code here

#!/usr/bin/env python3

import pygame as pg
import random

class Brick(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface( (100, 50) )
        r = random.randint
        self.image.fill( (r(0,254), r(0,254), r(0,254)) )
        self.rect = self.image.get_rect()
        #code used for randomly placing rectangle
        #not what we want, but could be used to reference placing more bricks
        #self.rect.x = random.randint(0,800)
        #self.rect.y  = random.randint(0,600)

class Game:
    def __init__(self):
        pg.init()
        self.__running = False
        self.screen = pg.display.set_mode ( (800, 600) )
        self.clock = pg.time.Clock()
        self.bricks = pg.sprite.Group()
        
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
            #Redraw
            self.screen.fill( (255, 255, 255) )
            self.bricks.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)

    def setRunning(self, running):
        self.__running = running

    def addBrick(self, brick):
        self.bricks.add(brick)
	
def main():
    game = Game()
    one = Brick()
    game.addBrick(one)
    game.setRunning(True)
    game.run()
	
if __name__ == '__main__':
    main()
