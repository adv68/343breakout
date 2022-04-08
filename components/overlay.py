import pygame as pg

class Overlay(pg.sprite.Sprite):
    def __init__(self):
        # initialize superclass
        super().__init__()

        self.image = pg.Surface( (800, 600), pg.SRCALPHA )
        #self.image.set_alpha(0)
        self.rect = self.image.get_rect()

        font = pg.font.Font(pg.font.get_default_font(), 16)
        scoreAndLives = font.render('Lives:     Score: ', True, (0,0,0), (255,255,255))
        
        scoreAndLivesRect = scoreAndLives.get_rect()
        scoreAndLivesRect.bottomleft = (25, 590)

        self.image.blit(scoreAndLives, scoreAndLivesRect)
        pg.display.update()
        

    def update(self):
        super().update(self)
        font = pg.font.Font(pg.font.get_default_font(), 16)
        scoreAndLives = font.render('Lives: '+str(self.ball.sprite.lives)+'    Score: '+str(self.ball.sprite.score), True, (0,0,0), (255,255,255))
        scoreAndLivesRect = scoreAndLives.get_rect()
        scoreAndLivesRect.bottomleft = (25, 590)

        self.image.blit(scoreAndLives, scoreAndLivesRect)
        pg.display.update()

        #not sure how much code is necessary for this function
        #we might have to add bricks to this class like for collision and ball
        #to keep track of score and somehow lives... will work on later
        
        #scoreAndLives = font.render('Lives:     Score: ', True, (0,0,0), (255,255,255))
        
        #scoreAndLivesRect = scoreAndLives.get_rect()
        #scoreAndLivesRect.bottomleft = (25, 580)

        #self.image.blit(scoreAndLives, scoreAndLivesRect)
        #pg.display.update()
        
