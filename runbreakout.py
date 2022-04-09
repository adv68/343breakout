#!/usr/bin/env python3

from components.game import Game
from components.brick import Brick
from components.bumper import Bumper
from random import randint

def main():
    # define game data
    width = 800
    height = 600

    # create game
    game = Game(width, height)
    
    # define level 1 bricks
    for i in range(0, 8):
        for j in range (0, 5):
            game.addBrick(Brick(100, 50, i * 100, j * 50))
    
    # run the game loop for level 1
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 1"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    #define level 2 bricks
    numBricks = 40
    minWidth = 60
    maxWidth = 150
    widthOffset = 0
    heightOffset = 0
    brickHeight = 50
    while numBricks > 0:
        if (widthOffset + maxWidth >= width):
            game.addBrick(Brick(width - widthOffset, brickHeight, widthOffset, heightOffset))
            heightOffset = heightOffset + brickHeight
            widthOffset = 0
        else: 
            w = randint(minWidth, maxWidth)
            game.addBrick(Brick(w, brickHeight, widthOffset, heightOffset))
            widthOffset = widthOffset + w
        numBricks = numBricks - 1

    # run game loop for level 2
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 2"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # game is over, no more levels
    game.gameMessage("You have won the game!", 5)
    game.dispose()
	
if __name__ == '__main__':
    main()
