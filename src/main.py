import pygame as pg
import pygame_menu as pgm
import threading
from Menu import Menu
from Bomb import Bomb
from Character import Character
from Mlevel import Level

# initialize the pygame
pg.init()

# setting screen height, width and accessible size
size = width, height = 900, 700
bRadX, bRadY = 10, 10
# create screen
screen = pg.display.set_mode((width, height))
# Initialize the pygame menu, comment out to work on game for now
menu = Menu(height, width, screen)


running = True
# game loop-ish
while running:
    menu.menu()
    pg.time.delay(100)

    # checks if there are events in the pygame window
    for event in pg.event.get():

        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False

        trigger = pg.key.get_pressed()

    pg.display.update()