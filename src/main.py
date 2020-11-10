import pygame as pg
from Menu import Menu
# import threading

# initialize the pygame
pg.init()

pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load('res/bomb3.png')
pg.display.set_icon(icon)

# Setting screen height, width and accessible size
size = width, height = 900, 700
# create screen
screen = pg.display.set_mode((width, height))
game_screen = pg.display.set_mode((width, height))
# Initialize the pygame menu
menu = Menu(height, width, screen, game_screen)


running = True
# game loop-ish
menu.menu()
while running:
    pg.time.wait(100)

    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False

    pg.display.update()
    menu.playButton()
