import pygame as pg
import pygame_menu as pgm
from Game import Game_handler as gh


class Menu:
    def __init__(self, menuW, menuH, surface, game_surface):
        self.menuH = menuH
        self.menuW = menuW
        self.surface = surface
        self.game_surface = game_surface

        # Initialize menus
        self.mainMenu = pgm.Menu(600, 500, "Welcome", theme=pgm.themes.THEME_SOLARIZED)
        self.itemShopMenu = pgm.Menu(600, 500, "Item Shop", theme=pgm.themes.THEME_SOLARIZED)
        self.settingsMenu = pgm.Menu(600, 500, "Settings", theme=pgm.themes.THEME_SOLARIZED)
        self.quitMenu = pgm.Menu(200, 200, "Quit", theme=pgm.themes.THEME_SOLARIZED)

        self.game = gh(self.game_surface)




    def draw_mainMenu(self):
        self.surface.fill((255, 255, 255))
        self.mainMenu.add_text_input('Name: ', default="")
        self.mainMenu.add_button('Play', self.start_game)
        self.mainMenu.add_button('Item shop', self.itemShopMenu)
        self.mainMenu.add_button('Settings', self.settingsMenu)
        self.mainMenu.add_button('Quit', self.quitMenu)
        self.mainMenu.mainloop(self.surface)

    def start_game(self):
        self.mainMenu.disable()
        self.game_surface.fill((0, 0, 0))
        self.game.draw()

    def draw_itemShopMenu(self):
        self.itemShopMenu.add_button("Go back", pgm.events.BACK)

    def draw_settingsMenu(self):
        self.settingsMenu.add_button("Go back", pgm.events.BACK)

    def draw_quitMenu(self):
        self.quitMenu.add_label("Are you sure?")
        self.quitMenu.add_button("Yes", pg.display.quit() and pg.quit())
        self.quitMenu.add_button("No", pgm.events.BACK)
        # Quits displaying on the surface
        pg.display.quit()
