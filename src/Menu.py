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

        self.menu_draw = pgm.Menu(self.menuX, self.menuY, 'Welcome', theme=pgm.themes.THEME_SOLARIZED)
        self.bomb_player_one = Bomb(10, 10, 300, 300, True, True, screen)
        self.char1 = Character(249, 149, screen)
        self.level = Level(0, 0, 0, 0, screen)

    def menu(self):
        self.menu_draw.add_text_input('Name: ')
        self.menu_draw.add_button('Play', self.playButton)
        self.menu_draw.add_button('Item shop', self.itemShop)
        self.menu_draw.add_button('Settings', self.settings)
        self.menu_draw.mainloop(self.screen)

    def playButton(self):
        self.menu_draw.disable()
        self.screen.fill((0, 0, 0))
        self.level.level()
        self.level.positional_grid()
        self.level.impassible_blocks()
        self.char1.player_movement()
        self.char1.draw_char()
        self.bomb_player_one.bomb()

    def itemShop(self):
        pass
    def settings(self):
        pass

    def exit(self):
        exit()
