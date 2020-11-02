import pygame as pg
import pygame_menu as pgm
import threading
from Bomb import Bomb
from Character import Character
from Mlevel import Level

class Menu:

    def __init__(self, menuX, menuY, screen):
        self.menuX = menuX
        self.menuY = menuY
        self.screen = screen

        # instantiating Bomb class
        self.bomb_player_one = Bomb(10, 10, True, 5, True)
        # instantiating Char class
        self.char1 = Character(249, 149, screen)
        self.level = Level(0, 0, 0, 0, screen)

    def menu(self):
        self.menu = pgm.Menu(self.menuX, self.menuY, 'Welcome', theme=pgm.themes.THEME_SOLARIZED)

        self.menu.add_text_input('Name: ')
        self.menu.add_button('Play', self.playButton())
        self.menu.mainloop(self.screen)


    def playButton(self):
        self.level.level()
        self.level.positional_grid()
        self.level.impassible_blocks()
        self.char1.draw_char()

    def itemShop(self):
        pass

    def settings(self):
        pass

    def exit(self):
        exit()
