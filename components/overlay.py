import pygame as pg

class Overlay(pg.sprite.Sprite):
    """ Overlay class
    
    The overlay class displays the score and lives on the bottom of the screen
    """
    
    def __init__(self, stats):
        """ Constructor for the Overlay class

        Creates a new Overlay which is descendent from pygame.sprite
        
        Arguments
        stats: a Stats object from components.stats
        """

        # initialize superclass
        super().__init__()

        # define sprite properties
        self.image = pg.Surface( (800, 600), pg.SRCALPHA )
        self.rect = self.image.get_rect()

        # copy stats object
        self._stats = stats

        # define font and render text for overlay
        self._font = pg.font.Font(pg.font.get_default_font(), 16)
        scoreAndLives = self._font.render('Lives:     Score: ', True, (0,0,0), (255,255,255))
        scoreAndLivesRect = scoreAndLives.get_rect()
        scoreAndLivesRect.bottomleft = (25, 590)

        # blit overlay text to the overlay image
        self.image.blit(scoreAndLives, scoreAndLivesRect)
        pg.display.update()        

    def update(self):
        """Sprite update method

        Used to update the sprites internal data before re-rendering to the screen
        """
        # call superclass update
        super().update(self)

        # render text for overlay
        scoreAndLives = self._font.render('Lives: ' + str(self._stats.getLives()) + '    Score: ' + str(self._stats.getScore()) + '  ', True, (0,0,0), (255,255,255))
        scoreAndLivesRect = scoreAndLives.get_rect()
        scoreAndLivesRect.bottomleft = (25, 590)

        # blit overlay text to the overlay image
        self.image.blit(scoreAndLives, scoreAndLivesRect)
        pg.display.update()
        