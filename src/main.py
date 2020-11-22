import pygame as pg
import pygame_menu as pgm
from game import GameHandler as gh
from client import Client
import const
from server import Server
import multiprocessing as mp


# method for starting game, passing player controls as args
def start_game(up, down, left, right, plant_bomb):
    # initialize pygame
    pg.init()

    # init surface from const.py
    surface = const.surface

    # instantiate client object with surface as argument
    client = Client(surface)

    # Set surface caption and icon
    pg.display.set_caption("Bomberman Spin-off Game")
    icon = pg.image.load('Res/bomb_icon.png')
    pg.display.set_icon(icon)

    # create menus via pygame_menu (pgm) library with properties
    # pgm is drawn (repeatedly) directly via connection to the pygame (pg) library,
    # so it does not need to be drawn in the game loop, neither does its widgets
    welcomeMenu = pgm.Menu(width=const.width, height=const.height, title="Bomberman Spin-off Game", enabled=True,
                           theme=pgm.themes.THEME_SOLARIZED)
    mainMenu = pgm.Menu(width=const.width, height=const.height, title="Welcome", enabled=True,
                        theme=pgm.themes.THEME_SOLARIZED)
    itemShopMenu = pgm.Menu(width=const.width, height=const.height, title="Item Shop", enabled=True,
                            theme=pgm.themes.THEME_SOLARIZED)
    settingsMenu = pgm.Menu(width=const.width, height=const.height, title="Settings", enabled=True,
                            theme=pgm.themes.THEME_SOLARIZED)
    quitMenu = pgm.Menu(width=const.width, height=const.height, title="Are you sure?", enabled=True,
                        theme=pgm.themes.THEME_SOLARIZED)

    # Font sizes for menu text
    fs1 = 40
    fs2 = 50
    spacing = 20

    # create widgets with properties for each menu

    # welcome menu
    welcomeMenu.add_image("res/title_img.png")
    welcomeMenu.add_label("Please enter your avatar name:", font_size=fs2)
    welcomeMenu.add_text_input("Name: ", default="", font_size=fs1)
    welcomeMenu.add_button("Go to main menu", mainMenu, font_size=fs1)

    # main menu

    # disable the welcome menu (highest in menu hierarchy) if the play button is pressed
    mainMenu.add_button("Play", welcomeMenu.disable, font_size=fs2)

    mainMenu.add_vertical_margin(spacing)
    mainMenu.add_button("Item Shop", itemShopMenu, font_size=fs2)
    mainMenu.add_vertical_margin(spacing)
    mainMenu.add_button("Settings", settingsMenu, font_size=fs2)
    mainMenu.add_vertical_margin(spacing)

    # navigate to upper level hierarchy menu (welcome menu)
    mainMenu.add_button("Change avatar name", pgm.events.RESET, font_size=fs2)
    mainMenu.add_vertical_margin(spacing)
    mainMenu.add_button("Quit", quitMenu, font_size=fs2)

    # item shop menu, not implemented
    itemShopMenu.add_label("Not implemented", font_size=fs2)
    itemShopMenu.add_vertical_margin(25)
    itemShopMenu.add_button("Go back", pgm.events.BACK, font_size=fs2)

    # settings menu, not implemented
    settingsMenu.add_label("Not implemented", font_size=fs2)
    settingsMenu.add_vertical_margin(25)
    settingsMenu.add_button("Go back", pgm.events.BACK, font_size=fs2)

    # quit menu for closing the program
    quitMenu.add_button("Yes", pgm.events.EXIT, font_size=fs2)
    quitMenu.add_button("No", pgm.events.BACK, font_size=fs2)

    # inst game object passing surface, client and controls as args
    game = gh(surface, client, up, down, left, right, plant_bomb)

    # boolean variable for creating another client
    run_once = True

    # bool variable that keeps the while loop running
    running = True
    while client.game_active:
        # delay for networking
        pg.time.wait(100)

        # checks if there are events in the pygame window
        events = pg.event.get()
        for event in events:
            # if the window closes, it gets closed properly
            if event.type == pg.QUIT:
                # closes the other client properly
                client.send(ACTION=const.CLIENT_QUIT)
                break
        # conditional that updates the menus if the welcome menu is enabled
        if welcomeMenu.is_enabled():
            welcomeMenu.draw(const.surface)
            welcomeMenu.update(events)
            pg.display.update()

        # if the menu is not enabled, run the game
        if not mainMenu.is_enabled():
            if run_once:
                # connect the other client
                client.send(ACTION=const.CLIENT_CONNECT)
                run_once = False
            # clear inactive menus and draw game
            welcomeMenu.clear()
            const.surface.fill((0, 0, 0))
            game.move()
            game.draw()
            pg.display.update()


# start server and clients
if __name__ == "__main__":
    server = Server()
    game2 = mp.Process(target=start_game, args=(pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE))
    game2.start()
    start_game(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_p)
