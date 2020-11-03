import pygame as pg
import pygame_menu as pgm
from Menu import Menu

import threading

from Mlevel import Level
from Character import Character
from Bomb import Bomb

# initialize the pygame
pg.init()

# setting screen height, width and accessible size
size = width, height = 900, 700
# create screen
screen = pg.display.set_mode((width, height))
# Initialize the pygame menu
menu = Menu(height, width, screen)

#Initialize char
# char1 = Character(int(width / 2), int(height / 2), screen)

running = True
# game loop-ish
while running:

    pg.time.delay(100)

    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
    menu.menu()
    menu.playButton()
    pg.display.update()
