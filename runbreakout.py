#!/usr/bin/env python3

from components.game import Game
from components.brick import Brick
from components.bumper import Bumper
from random import randint

def main():
    # create game
    game = Game(800, 600)

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

    # define level 2 bricks
    width = 800
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
    
    # define level 3 bricks
    width = 800
    maxHeightOffset = 300
    minWidth = 60
    maxWidth = 150
    widthOffset = 0
    heightOffset = 0
    brickHeight = 50
    while heightOffset <= maxHeightOffset:
        if (widthOffset + maxWidth >= width):
            game.addBrick(Brick(width - widthOffset, brickHeight, widthOffset, heightOffset))
            heightOffset = heightOffset + brickHeight
            widthOffset = 0
        else: 
            w = randint(minWidth, maxWidth)
            game.addBrick(Brick(w, brickHeight, widthOffset, heightOffset))
            widthOffset = widthOffset + w

    # run game loop for level 3
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 3"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    #define level 4 bricks
    for i in range(0, 6):
        for j in range(0, 4):
            game.addBrick(Brick(50, 100, i * 50, j * 100))
            game.addBrick(Brick(50, 100, (i * 50) + 500, j * 100))

    # run game loop for level 4
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 4"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # define level 5 bricks
    for i in range(0, 8):
        for j in range (0, 5):
            game.addBrick(Brick(100, 50, i * 100, j * 50))
    game.addBrick(Bumper(75, 50, 0, 300))
    game.addBrick(Bumper(300, 50, 250, 300))
    game.addBrick(Bumper(75, 50, 725, 300))
    
    # run the game loop for level 5
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 5"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # define level 6 bricks
    for i in range(8, 0, -1):
        for j in range(0, i):
            game.addBrick(Brick(100, 50, j * 100 + ((800 - (i * 100)) / 2), (-i + 8) * 50))
    game.addBrick(Bumper(300, 50, 250, 400))

    # run the game loop for level 6
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 6"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return
    
    # define level 7 bricks
    for i in range(4, 0, -1):
        for j in range(0, i):
            game.addBrick(Brick(100, 50, j * 100 + ((400 - (i * 100)) / 2), (-i + 4) * 50))
            game.addBrick(Brick(100, 50, j * 100 + ((400 - (i * 100)) / 2) + 400, (-i + 4) * 50))
    game.addBrick(Bumper(200, 50, 0, 300))
    game.addBrick(Bumper(200 ,50, 600, 300))

    # run the game loop for level 7
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 7"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # define level 8 bricks
    for i in range(0, 8):
        for j in range(0, 3):
            game.addBrick(Brick(50, 100, i * 50 + 200, j * 100))
    game.addBrick(Bumper(400, 50, 200, 300))
    for i in range(0, 4):
        game.addBrick(Brick(100, 50, i * 100 + 200, 350))

    # run the game loop for level 8
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 8"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # define level 9 bricks
    for i in range(0, 8):
        for j in range(0, 3):
            game.addBrick(Brick(50, 50, i * 50 + 200, j * 50))
    for i in range(0, 3):
        for j in range(0, 4):
            game.addBrick(Brick(50, 100, i * 50, j * 100))
            game.addBrick(Brick(50, 100, (i * 50) + 650, j * 100))
    game.addBrick(Bumper(200, 50, 0, 400))
    game.addBrick(Bumper(200, 50, 600, 400))

    # run the game loop for level 9
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 9"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # define level 10 bricks
    for i in range(0, 16):
        for j in range(0, 2):
            game.addBrick(Brick(50, 50, i * 50, j * 50))
    for i in range(4, 0, -1):
        for j in range(0, i):
            game.addBrick(Brick(100, 50, j * 100 + ((400 - (i * 100)) / 2), (-i + 8) * 50))
            game.addBrick(Brick(100, 50, j * 100 + ((400 - (i * 100)) / 2) + 400, (-i + 8) * 50))
    game.addBrick(Bumper(300, 50, 250, 125))
    game.addBrick(Bumper(200, 50, 300, 400))

    # run the game loop for level 10
    # if the run loop returns false, then do not proceed to the next level
    if not game.run("Level 10"):
        game.gameMessage("Goodbye", 2)
        game.dispose()
        return

    # game is over, no more levels
    game.gameMessage("You have won the game!", 5)
    game.dispose()
	
if __name__ == '__main__':
    main()
