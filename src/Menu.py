import pygame as pg
import pygame_menu as pgm
# import threading
from Bomb import Bomb
from Character import Character
from Mlevel import Level


class Menu:
    def __init__(self, menuH, menuW, surface):
        self.menuH = menuH
        self.menuW = menuW
        self.surface = surface

        # Initialize menus
        self.mainMenu = pgm.Menu(600, 500, "Welcome", theme=pgm.themes.THEME_SOLARIZED)
        self.itemShopMenu = pgm.Menu(600, 500, "Item Shop", theme=pgm.themes.THEME_SOLARIZED)
        self.settingsMenu = pgm.Menu(600, 500, "Settings", theme=pgm.themes.THEME_SOLARIZED)
        self.quitMenu = pgm.Menu(200, 200, "Quit", theme=pgm.themes.THEME_SOLARIZED)

        # Initialize game objects
        self.char1 = Character(249, 149, surface)
        self.bomb_player_one = Bomb(10, 10, 300, 300, True, True, surface)
        self.level = Level(0, 0, 0, 0, surface)

    def draw_background(self):
        self.surface.fill((255, 255, 255))

    def draw_mainMenu(self):
        self.mainMenu.add_text_input('Name: ', default="")
        self.mainMenu.add_button('Play', self.playButton)
        self.mainMenu.add_button('Item shop', self.itemShopMenu)
        self.mainMenu.add_button('Settings', self.settingsMenu)
        self.mainMenu.add_button('Quit', self.quitMenu)
        self.mainMenu.mainloop(self.surface)

    def playButton(self):
        self.mainMenu.disable()

        self.surface.fill((0, 0, 0))
        self.level.level()
        self.level.positional_grid()
        self.level.impassible_blocks()
        self.char1.player_movement()
        self.char1.draw_char()
        self.bomb_player_one.bomb(self.char1.posX, self.char1.posY)

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