import pygame as pg
from Menu import Menu

if __name__ == '__main__':

    # initialize pygame
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
    menu.draw_mainMenu()
    # menu.draw_itemShopMenu()
    # menu.draw_settingsMenu()
    # menu.draw_quitMenu()

    # boolean variable that keeps the while loop running
    running = True
    while running:
        # runs when the play button in the menu is pressed
        menu.start_game()
        # delay so the game is slower
        pg.time.wait(100)

        # checks if there are events in the pygame window
        events = pg.event.get()
        for event in events:
            # if the window closes, it gets closed properly
            if event.type == pg.QUIT:
                running = False

        if menu.mainMenu.is_enabled():
            menu.mainMenu.update(events)
            menu.mainMenu.draw_bomb(surface)
            menu.mainMenu.mainloop(surface, bgfun=menu.draw_background)

            menu.mainMenu.mainloop(surface)
        # updates the display of the pygame window
        pg.display.update()