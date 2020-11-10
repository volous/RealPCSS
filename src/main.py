import pygame as pg
from Menu import Menu
# import threading


# Initialize pygame surface
pg.init()

# Set caption and icon
pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load('res/bomb3.png')
pg.display.set_icon(icon)

# Setting screen height, width and accessible size
size = width, height = 900, 700
# Create surface
surface = pg.display.set_mode((width, height))

# Init menu
menu = Menu(height, width, surface)


running = True
while running:
    menu.draw_background()
    menu.draw_mainMenu()
    menu.draw_itemShopMenu()
    menu.draw_settingsMenu()
    menu.draw_quitMenu()

    pg.time.delay(100)

    # checks if there are events in the pygame window
    events = pg.event.get()
    for event in events:
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False

    if menu.mainMenu.is_enabled():
        menu.mainMenu.update(events)
        menu.mainMenu.draw(surface)
        menu.mainMenu.mainloop(surface, bgfun=menu.draw_background)
        pg.display.update()