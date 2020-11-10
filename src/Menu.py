import pygame as pg
import pygame_menu as pgm
# import threading
from Bomb import Bomb
from Character import Character
from Mlevel import Level


class Menu:
    def __init__(self, menuH, menuW, screen):
        self.menuH = menuH
        self.menuW = menuW
        self.screen = screen

        # Initialize menus
        self.mainMenu_draw = pgm.Menu(self.menuH, self.menuW, 'Welcome', theme=pgm.themes.THEME_SOLARIZED)
        self.settings_draw = pgm.Menu(self.menuH, self.menuW, 'Settings', theme=pgm.themes.THEME_SOLARIZED)

        # Initialize game objects
        self.char1 = Character(249, 149, screen)
        self.bomb_player_one = Bomb(10, 10, 300, 300, True, True, screen)
        self.level = Level(0, 0, 0, 0, screen)

    def mainMenu(self):
        self.mainMenu_draw.add_text_input('Name: ')
        self.mainMenu_draw.add_button('Play', self.playButton)
        self.mainMenu_draw.add_button('Item shop', self.itemShop)
        self.mainMenu_draw.add_button('Settings', self.settings)
        self.mainMenu_draw.add_button('Quit', self.exit)
        self.mainMenu_draw.mainloop(self.screen)

    def playButton(self):
        self.mainMenu_draw.disable()
        self.screen.fill((0, 0, 0))
        self.level.level()
        self.level.positional_grid()
        self.level.impassible_blocks()
        self.char1.player_movement()
        self.char1.draw_char()
        self.bomb_player_one.bomb(self.char1.posX, self.char1.posY)

    def itemShop(self):
        pass

    def settings(self):
        self.mainMenu_draw.disable()




    def exit(self):
        # Quits displaying on the surface
        pg.display.quit()
        # Quits the surface
        pg.quit()

