import pygame as pg
from Menu import Menu
# import threading

# initialize the pygame
pg.init()

# Set caption and icon
pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load('res/bomb3.png')
pg.display.set_icon(icon)

# Create surface from dimensions
width, height = 900, 700
surface = pg.display.set_mode((width, height))
game_surface = pg.display.set_mode((width, height))
# Instantiate the pygame menu
menu = Menu(height, width, surface, game_surface)

# pygame_menu handles draws itself, so no need to put it in the loop
menu.draw_background()
menu.draw_mainMenu()
# menu.draw_itemShopMenu()
# menu.draw_settingsMenu()
# menu.draw_quitMenu()

running = True
while running:
    menu.start_game()

    pg.time.wait(100)

    # checks if there are events in the pygame window
    events = pg.event.get()
    for event in events:
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

    if menu.mainMenu.is_enabled():
        menu.mainMenu.update(events)
        menu.mainMenu.draw(surface)

        menu.mainMenu.mainloop(surface, bgfun=menu.draw_background)
