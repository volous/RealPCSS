import pygame as pg
import pygame_menu as pgm
from Character import Character
from Mlevel import Level


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

        # Initialize level and characters
        self.level = Level(0, 0, 0, 0, self.game_surface)
        self.level.level()
        self.level.impassible_blocks()
        self.char1 = Character(1, 1, 249, 149, self.game_surface, self.level.walkable, (255, 0, 0))

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
        self.game_surface.fill((0, 0, 0))
        self.level.draw_level()
        self.char1.player_actions()
        self.char1.draw_char()

    def draw_itemShopMenu(self):
        self.itemShopMenu.add_button("Go back", pgm.events.BACK)

    def draw_settingsMenu(self):
        self.settingsMenu.add_button("Go back", pgm.events.BACK)

    def draw_quitMenu(self):
        self.quitMenu.add_label("Are you sure?")
        self.quitMenu.add_button("Yes", pg.quit())
        self.quitMenu.add_button("No", pgm.events.BACK)
        # Quits displaying on the surface
        pg.display.quit()
