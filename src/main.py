import pygame as pg
import pygame_menu as pgm
from game import Game_handler as gh
from client import Client
import const
from server import Server
import multiprocessing as mp


def start_game(up, down, left, right, plant_bomb):
    # initialize pygame
    pg.init()

    surface = const.surface
    client = Client(surface)
    # Set caption and icon
    pg.display.set_caption("Bomberman Spin-off Game")
    icon = pg.image.load('res/bomb3.png')
    pg.display.set_icon(icon)

    # init menus
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

    fs1 = 40
    fs2 = 50

    w_widget1 = welcomeMenu.add_image("res/title_img.png")
    w_widget2 = welcomeMenu.add_label("Please enter your avatar name:", font_size=fs2)
    w_widget3 = welcomeMenu.add_text_input("Name: ", default="", font_size=fs1)
    w_widget4 = welcomeMenu.add_button("Go to main menu", mainMenu, font_size=fs1)

    m_spacing = 20
    m_widget2 = mainMenu.add_button("Play", welcomeMenu.disable, font_size=fs2)
    mainMenu.add_vertical_margin(m_spacing)
    m_widget3 = mainMenu.add_button("Item Shop", itemShopMenu, font_size=fs2)
    mainMenu.add_vertical_margin(m_spacing)
    m_widget4 = mainMenu.add_button("Settings", settingsMenu, font_size=fs2)
    mainMenu.add_vertical_margin(m_spacing)
    m_widget5 = mainMenu.add_button("Change avatar name", pgm.events.RESET, font_size=fs2)
    mainMenu.add_vertical_margin(m_spacing)
    m_widget6 = mainMenu.add_button("Quit", quitMenu, font_size=fs2)

    i_widget1 = itemShopMenu.add_label("Not yet implemented", font_size=fs2)
    itemShopMenu.add_vertical_margin(25)
    i_widget2 = itemShopMenu.add_button("Go back", pgm.events.BACK, font_size=fs2)

    i_widget1 = settingsMenu.add_label("Not yet implemented", font_size=fs2)
    settingsMenu.add_vertical_margin(25)
    s_widget2 = settingsMenu.add_button("Go back", pgm.events.BACK, font_size=fs2)

    q_widget1 = quitMenu.add_button("Yes", pgm.events.EXIT, font_size=fs2)
    q_widget2 = quitMenu.add_button("No", pgm.events.BACK, font_size=fs2)

    game = gh(surface, client, up, down, left, right, plant_bomb)
    run_once = True

    # boolean variable that keeps the while loop running
    running = True
    while client.game_active:
        # delay so the game is slower
        pg.time.wait(100)

        # checks if there are events in the pygame window
        events = pg.event.get()
        for event in events:
            # if the window closes, it gets closed properly
            if event.type == pg.QUIT:
                client.send(ACTION=const.CLIENT_QUIT)
                break

        if welcomeMenu.is_enabled():
            welcomeMenu.draw(const.surface)
            welcomeMenu.update(events)

        if not mainMenu.is_enabled():
            if run_once:
                client.send(ACTION=const.CLIENT_CONNECT)
                run_once = False
            mainMenu.disable()
            const.surface.fill((0, 0, 0))
            game.move()
            game.draw()
            pg.display.update()

        # updates the display of the pygame window
        pg.display.update()


if __name__ == "__main__":

    server = Server()
    game2 = mp.Process(target=start_game, args=(pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE))
    game2.start()
    start_game(pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_p)

