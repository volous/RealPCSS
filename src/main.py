import pygame as pg
import pygame_menu as pgm
from Menu import Menu
# import threading



# Initialize the pygame
pg.init()

pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load('res/bomb3.png')
pg.display.set_icon(icon)

# Setting screen height, width and accessible size
size = width, height = 900, 700
# Create surface
surface = pg.display.set_mode((width, height))
# Initialize the pygame menu, pgm.Menu() takes height before width
menu = Menu(height, width, surface)

running = True
# game loop-ish

while running:
    pg.time.delay(100)

    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
    menu.mainMenu()
    menu.playButton()


    pg.display.update()


