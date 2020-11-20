import pygame as pg
import pygame_menu as pgm
from Game import Game_handler as gh
from Network import Network
import player_id


def draw_menus():
    imgPath = "res/img.jpg"
    mainMenu.add_image(imgPath)

    # Get text input value using: print("Hi " + widget1.get_value() + "!")
    m_widget1 = mainMenu.add_text_input("Name: ", default="")
    m_widget2 = mainMenu.add_button("Play", mainMenu.disable)
    m_widget3 = mainMenu.add_button("Item Shop", itemShopMenu)
    m_widget4 = mainMenu.add_button("Settings", settingsMenu)
    m_widget5 = mainMenu.add_button("Quit", quitMenu)

    i_widget1 = itemShopMenu.add_button("Go back", pgm.events.BACK)
    s_widget1 = settingsMenu.add_button("Go back", pgm.events.BACK)
    q_widget1 = quitMenu.add_button("Yes", pgm.events.EXIT)
    q_widget2 = quitMenu.add_button("No", pgm.events.BACK)


if __name__ == '__main__':
    # initialize pygame
    pg.init()



    # Set caption and icon
    pg.display.set_caption("Bomberman Spin-off Game")
    icon = pg.image.load('res/bomb3.png')
    pg.display.set_icon(icon)

    # init menus
    mainMenu = pgm.Menu(width=player_id.width, height=player_id.height, title="Welcome", enabled=True, theme=pgm.themes.THEME_SOLARIZED)
    itemShopMenu = pgm.Menu(width=player_id.width, height=player_id.height, title="Item Shop", enabled=True, theme=pgm.themes.THEME_SOLARIZED)
    settingsMenu = pgm.Menu(width=player_id.width, height=player_id.height, title="Settings", enabled=True, theme=pgm.themes.THEME_SOLARIZED)
    quitMenu = pgm.Menu(width=player_id.width, height=player_id.height, title="Are you sure?", enabled=True, theme=pgm.themes.THEME_SOLARIZED)



    # Draw the main menu and submenus
    draw_menus()



    game = gh(player_id.surface)
    # boolean variable that keeps the while loop running
    running = True
    while running:
        # delay so the game is slower
        pg.time.wait(100)
        p2 = n.send(p)

        # checks if there are events in the pygame window
        events = pg.event.get()
        for event in events:
            # if the window closes, it gets closed properly
            if event.type == pg.QUIT:
                running = False

        if mainMenu.is_enabled():
            mainMenu.draw(player_id.surface)
            mainMenu.update(events)

        if not mainMenu.is_enabled():
            mainMenu.disable()
            player_id.surface.fill((0, 0, 0))
            game.draw()
            pg.display.update()

        # updates the display of the pygame window
        pg.display.update()
