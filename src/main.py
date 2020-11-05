import pygame as pg
import pygame_menu as pgm
from Menu import Menu
# import threading

# Initialize the pygame
pg.init()

# Setting screen height, width and accessible size
size = width, height = 900, 700
# Create surface
surface = pg.display.set_mode((width, height))
# Initialize the pygame menu, pgm.Menu() takes height before width
menu = Menu(height, width, surface)

running = True
# game loop-ish
try:
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
except:
    print("game did not run")

pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load('res/bomb3.png')
pg.display.set_icon(icon)

menu = Menu(height, width, surface)
# Initialize character1
# char1 = Character(int(width / 2), int(height / 2), screen)



running = True
# Game loop
while running:

    pg.time.delay(100)

    # Checks if there are events in the pygame window
    for event in pg.event.get():
        # If the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False

    menu.mainMenu()
    menu.playButton()
    menu.itemShop()
    menu.settings()
    menu.exit()

    # Updates the surface display
    pg.display.update()

