import pygame as pg
from Network import Network
from Game import Game_handler as gh
import constants


if __name__ == '__main__':
    # initialize pygame
    pg.init()
    n = Network()
    p = n.getP()

    width, height = 700, 900

    screen = pg.display.set_mode(width, height)
    # Set caption and icon
    pg.display.set_caption("Bomberman Spin-off Game")
    icon = pg.image.load('res/bomb3.png')
    pg.display.set_icon(icon)

    game = gh(screen)


    # boolean variable that keeps the while loop running
    running = True
    while running:
        # delay so the game is slower
        pg.time.wait(100)

        # checks if there are events in the pygame window
        events = pg.event.get()
        for event in events:
            # if the window closes, it gets closed properly
            if event.type == pg.QUIT:
                running = False
        p2 = n.send(p)
        screen.fill(0, 0, 0)
        game.draw()

        # updates the display of the pygame window
        pg.display.update()
