#!/usr/bin/env python3

from components.paddle import Paddle
from components.game import Game
from components.ball import Ball
from components.brick import Brick
from components.overlay import Overlay

def main():
    # define game data
    width = 800
    height = 600
    brickWidth = 100
    brickHeight = 50
    numBricksX = 8
    numBricksY = 5
    paddleSpeed = 8 # pixels per cycle @ 60Hz

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
    for i in range(0, numBricksX):
        for j in range (0, numBricksY):
            game.addBrick(Brick(i * brickWidth, j * brickHeight))

    # add paddle
    game.setPaddle(Paddle(width / 5, paddleSpeed))

    # add ball
    game.setBall(Ball())

    #add overlay
    game.setOverlay(Overlay())

    # tell the ball who the bricks are with the getter
    Ball.bricks = game.getBricks()

    # same as above but for paddle
    Ball.paddle = game.getPaddle()

    # start game  
    game.setRunning(True)
    game.run()
	
if __name__ == '__main__':
    main()
