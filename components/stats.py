class Stats:
    """ Stats class
    
    Stores statistics for the game
    Provides a wrapper for the score and lives so a reference to 
    the stats object can be passed between classes
    """

    def __init__(self, lives, score):
        """ Constructor for the Stats class

        Arguments
        lives: the initial value for lives
        score: the initial value for score
        """
        self._lives = lives
        self._score = score

    def setLives(self, lives):
        """ Set the value of lives """
        self._lives = lives

    def getLives(self):
        """ Get the value of lives """
        return self._lives

    def decrementLives(self):
        """ Decrement the value of lives (Subtract 1)"""
        self._lives = self._lives - 1

    def incrementLives(self):
        """ Increment the value of lives (Add 1) """
        self._lives = self._lives + 1

    def setScore(self, score):
        """ Set the value of score """
        self._score = score

    def getScore(self):
        """ Get the value of score """
        return self._score

    def appendScore(self, scoreToAdd):
        """ Add scoreToAdd to the current score """
        self._score = self._score + scoreToAdd