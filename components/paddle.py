import pygame as pg

class Paddle(pg.sprite.Sprite):
    def __init__(self, width, speed):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (width, 10) )
        self.image.fill( (0, 0, 0) )
        self.width = width

        self.rect = self.image.get_rect()
        self.rect.x = 400 - (width / 2)
        self.rect.y = 550

        self.speed = speed

    def setPosition(self, x):
        """
        Set the position of the paddle
        Coordinates are based off of the center of the paddle
        SO... if the paddle is 200px wide and the x-pos is 100, the paddle will touch the edge
        """
        self.rect.x = x - (self.width / 2)

    def getPosition(self):
        return self.rect.x + (self.width / 2)

    def update(self):
        super().update(self)

        mouseX, _ = pg.mouse.get_pos()

        if mouseX <= self.width / 2:
            mouseX = self.width / 2
        elif mouseX >= 800 - self.width / 2:
            mouseX = 800 - self.width / 2


        if abs(mouseX - self.getPosition()) >= self.speed:
            if mouseX < self.getPosition():
                self.setPosition(self.getPosition() - self.speed)
            elif mouseX > self.getPosition():
                self.setPosition(self.getPosition() + self.speed)

        #self.setPosition(mouseX)