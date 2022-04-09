class Stats:
    def __init__(self, lives, score):
        self._lives = lives
        self._score = score

    def setLives(self, lives):
        self._lives = lives

    def getLives(self):
        return self._lives

    def decrementLives(self):
        self._lives = self._lives - 1

    def incrementLives(self):
        self._lives = self._lives + 1

    def setScore(self, score):
        self._score = score

    def getScore(self):
        return self._score

    def appendScore(self, scoreToAdd):
        self._score = self._score + scoreToAdd