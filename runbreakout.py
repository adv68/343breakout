#!/usr/bin/env python3

from random import randint, random
from components.paddle import Paddle
from components.game import Game
from components.ball import Ball
from components.brick import Brick
from components.overlay import Overlay
from components.bumper import Bumper
from time import sleep

def main():
    # define game data
    width = 800
    height = 600
    brickWidth = 100
    brickHeight = 50
    numBricksX = 8
    numBricksY = 5
    paddleSpeed = 8 # pixels per cycle @ 60Hz
    ballSize = 9

    # validate data
    if (width % brickWidth != 0):
        raise Exception("Illegal brick width - game board width must be evenly divisible into bricks")
    if (numBricksX * brickWidth > width):
        raise Exception("Illegal brick width or X qty - number of bricks exceeds the game board width")
    if (numBricksY * brickHeight > height - 200):
        raise Exception("Illegal brick height or Y qty - number of bricks is to tall to be playable")

    # create game
    game = Game(width, height)
    
    # add bricks to the game
    '''
    for i in range(0, numBricksX):
        for j in range (0, numBricksY):
            game.addBrick(Brick(brickWidth, brickHeight, i * brickWidth, j * brickHeight))
    '''
    #-------------------------------------------------------------
    numBricks = 1
    minWidth = 60
    maxWidth = 150
    widthOffset = 0
    heightOffset = 0
    while numBricks > 0:
        if (widthOffset + maxWidth >= width):
            game.addBrick(Brick(width - widthOffset, brickHeight, widthOffset, heightOffset))
            heightOffset = heightOffset + brickHeight
            widthOffset = 0
        else: 
            w = randint(minWidth, maxWidth)
            b = randint(1, 2)
            if b == 1:
                game.addBrick(Brick(w, brickHeight, widthOffset, heightOffset))
            else:
                game.addBrick(Bumper(w, brickHeight, widthOffset, heightOffset))
            widthOffset = widthOffset + w
        numBricks = numBricks - 1
    #-------------------------------------------------------------

    # add paddle
    game.setPaddle(Paddle(width / 5, paddleSpeed))

    # add ball
    game.setBall(Ball(ballSize))

    #add overlay
    game.setOverlay(Overlay())

    # tell the ball who the bricks are with the getter
    Ball.bricks = game.getBricks()

    # same as above but for paddle
    Ball.paddle = game.getPaddle()

    # start game  
    game.run()
    #game.dispose()
    game.stop()

    sleep(5)
    game.addBrick(Brick(100, 100, 0, 0))
    game.setPaddle(Paddle(width / 5, paddleSpeed))
    game.setBall(Ball(ballSize))
    game.setOverlay(Overlay())
    Ball.bricks = game.getBricks()
    Ball.paddle = game.getPaddle()
    game.run()

    game.dispose()
	
if __name__ == '__main__':
    main()
